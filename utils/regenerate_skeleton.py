import argparse
import os
import shlex
import subprocess

import requests
from modify_skeleton import modify_schema, modify_skeleton

# Using a version from the branch
LOCAL_SCHEMA = "iiif_3_0.json"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Prezi3 Skeleton regeneration"
    )
    # Positional argument (required)
    parser.add_argument("--branch", default="main", help="IIIF presentation-validator branch to get the schema from")

    # Boolean flag (on/off)
    parser.add_argument("--yes", "-y", action="store_true",
                        help="Skip warning about replacing Skeleton")
    parser.add_argument("--local", "-l", action="store_true",
                        help="Use local current_schema.json instead of fetching from remote")

    args = parser.parse_args()

    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    skeleton_file = os.path.join(project_dir, "iiif_prezi3", "skeleton.py")

    if not args.yes:
        print("== Prezi3 Skeleton Regenerator ==")
        safety = input(f"WARNING: This will overwrite the existing Skeleton ({skeleton_file}) in-place. Continue y/n? ")

        if safety.lower() != "y":
            exit()

    REMOTE_SCHEMA_LOCATION = f"https://raw.githubusercontent.com/markpbaggett/presentation-validator/refs/heads/w3c-web-annotations/schema/iiif_3_0.json"
    LOCAL_SCHEMA_PATH = os.path.join(project_dir, "current_schema.json")
    DATAMODEL_COMMAND = f"datamodel-codegen --input {LOCAL_SCHEMA} --input-file-type jsonschema --use-default --remove-special-field-name-prefix --strict-nullable --base-class .base.Base --use-title-as-name --output-model-type pydantic_v2.BaseModel --output {skeleton_file}"

    if args.local:
        print(f"Using local schema file: {LOCAL_SCHEMA_PATH}")
        if not os.path.exists(LOCAL_SCHEMA_PATH):
            print(f"Error: Local schema file not found at {LOCAL_SCHEMA_PATH}")
            exit()
        import shutil
        shutil.copy(LOCAL_SCHEMA_PATH, LOCAL_SCHEMA)
    else:
        print(f"Downloading latest JSON Schema from the {args.branch} branch...")
        js = requests.get(REMOTE_SCHEMA_LOCATION)
        if js.status_code == 200:
            with open(LOCAL_SCHEMA, "wb") as out:
                out.write(js.content)
        else:
            print(f"Error retrieving JSON Schema - Status {js.status_code}")
            exit()

    modify_schema(LOCAL_SCHEMA)

    print("Generating Skeleton file...")
    subprocess.run(shlex.split(DATAMODEL_COMMAND), check=True)

    print("Running Skeleton modifications...")
    modify_skeleton(skeleton_file)

    print("Cleaning up Schema file...")
    os.remove(LOCAL_SCHEMA)

    print("Done!")
