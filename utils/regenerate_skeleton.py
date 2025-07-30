import os
import shlex
import subprocess

import requests
from modify_skeleton import modify_skeleton, modify_schema

# Using a version from the branch 
LOCAL_SCHEMA="iiif_3_0.json"
SCHEMA_LOCATION = "https://raw.githubusercontent.com/IIIF/presentation-validator/refs/heads/iiif-prezi-schema-update/schema/iiif_3_0.json"
DATAMODEL_COMMAND = f"datamodel-codegen --input {LOCAL_SCHEMA} --input-file-type jsonschema --use-default --remove-special-field-name-prefix --strict-nullable --base-class .base.Base --use-title-as-name --output ../iiif_prezi3/skeleton.py"

if __name__ == "__main__":
    print("== Prezi3 Skeleton Regenerator ==")
    safety = input("WARNING: This will overwrite the existing Skeleton in-place. Continue y/n? ")

    if safety.lower() != "y":
        exit()

    print("Downloading latest JSON Schema...")
    js = requests.get(SCHEMA_LOCATION)
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
    modify_skeleton()

    print("Cleaning up Schema file...")
    os.remove(LOCAL_SCHEMA)

    print("Done!")
