import os
import shlex
import subprocess

import requests
from modify_skeleton import modify_skeleton

SCHEMA_LOCATION = "https://raw.githubusercontent.com/IIIF/presentation-validator/main/schema/iiif_3_0.json"
DATAMODEL_COMMAND = "datamodel-codegen --input iiif_3_0.json --input-file-type jsonschema --use-default --remove-special-field-name-prefix --base-class .base.Base  --output ../iiif_prezi3/skeleton.py"

if __name__ == "__main__":
    print("== Prezi3 Skeleton Regenerator ==")
    safety = input("WARNING: This will overwrite the existing Skeleton in-place. Continue y/n? ")

    if safety.lower() != "y":
        exit()

    print("Downloading latest JSON Schema...")
    js = requests.get(SCHEMA_LOCATION)
    if js.status_code == 200:
        with open("iiif_3_0.json", "wb") as out:
            out.write(js.content)
    else:
        print(f"Error retrieving JSON Schema - Status {js.status_code}")
        exit()

    print("Generating Skeleton file...")
    subprocess.run(shlex.split(DATAMODEL_COMMAND), check=True)

    print("Running Skeleton modifications...")
    modify_skeleton()

    print("Cleaning up Schema file...")
    os.remove("iiif_3_0.json")

    print("Done!")
