import os
import shlex
import subprocess
import json

import requests
from modify_skeleton import modify_skeleton

SCHEMA_LOCATION = "https://raw.githubusercontent.com/IIIF/presentation-validator/issue-154/schema/iiif_3_0.json"
SCHEMA_FILENAME = "iiif_3_0.json"
DATAMODEL_COMMAND = "datamodel-codegen --input {} --input-file-type jsonschema --use-default --remove-special-field-name-prefix --strict-nullable --base-class .base.Base  --output ../iiif_prezi3/skeleton.py".format(SCHEMA_FILENAME)

def downgradeSchema(schema, filename):
    runSubstitute(schema)

    #print(json.dumps(schema, indent=4))
    with open(SCHEMA_FILENAME, "w") as out:
            out.write(json.dumps(schema, indent=4))

def runSubstitute(schema):    
    if isinstance(schema, list):
        for index, item in enumerate(schema):
            if isinstance(item, dict) and 'if' in item:
                if 'else' in item:
                    schema[index] = { 'oneOf': [
                        item['then'],
                        item['else']
                    ]}
                else:
                    schema[index] = item['then']

            #print ('recursive on list item ')
            #print(schema[index])
            runSubstitute(schema[index])

    if isinstance(schema,dict):        
        if 'allOf' in schema and "if" in schema['allOf'][0]:
            # We have an all of if statement 
            oneOf = []
            for statement in schema['allOf']:
                oneOf.append(statement["then"])
            del schema['allOf']
            schema['oneOf'] = oneOf

        
        for key in schema:
            if isinstance(schema[key],dict) and 'if' in schema[key]:
                if 'else' in schema[key]:
                    schema[key] = { 'oneOf': [
                        schema[key]['then'],
                        schema[key]['else']
                    ]}
                else:
                    schema[key] = schema[key]['then']

            if isinstance(schema[key],dict) or isinstance(schema[key],list):
                #print ('recursive on ' + key)
                #print (schema[key])
                runSubstitute(schema[key])

if __name__ == "__main__":
    print("== Prezi3 Skeleton Regenerator ==")
    safety = input("WARNING: This will overwrite the existing Skeleton in-place. Continue y/n? ")

    if safety.lower() != "y":
        exit()

    print("Downloading latest JSON Schema..." + SCHEMA_LOCATION)
    js = requests.get(SCHEMA_LOCATION)
    if js.status_code != 200:
        print(f"Error retrieving JSON Schema - Status {js.status_code}")
        exit()

    downgradeSchema(json.loads(js.content),SCHEMA_FILENAME)
   # with open('test.json') as tst_file:
    #    downgradeSchema(json.loads(tst_file.read()),SCHEMA_FILENAME)

    print("Generating Skeleton file...")
    subprocess.run(shlex.split(DATAMODEL_COMMAND), check=True)

    print("Running Skeleton modifications...")
    modify_skeleton()

    print("Cleaning up Schema file...")
    os.remove(SCHEMA_FILENAME)

    print("Done!")
