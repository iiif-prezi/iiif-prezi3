import json

CHANGES = [
    {
        "description": "Allow extra properties on Annotations",
        "type": "replace",
        "find": "\n\nclass Annotation(Class):",
        "replace": "\n\nclass Annotation(Class):\n    model_config = ConfigDict(extra='allow')\n"
    },
    {
        "description": "Allow extra properties on ServiceV3",
        "type": "replace",
        "find": "\n\nclass ServiceV3(Class):",
        "replace": "\n\nclass ServiceV3(Class):\n    model_config = ConfigDict(extra='allow')\n"
    },
    {
        "description": "Allow extra properties on ServiceV2",
        "type": "replace",
        "find": "\n\nclass ServiceV2(Base):",
        "replace": "\n\nclass ServiceV2(Base):\n    model_config = ConfigDict(extra='allow')\n"
    },
    {
        "description": "Allow extra properties on Reference",
        "type": "replace",
        "find": "\n\nclass Reference(Base):",
        "replace": "\n\nclass Reference(Base):\n    model_config = ConfigDict(extra='allow')\n"
    }

    #   {
 #       "description": "Re-add RangeRef",
 #       "type": "insert",
 #       "before": "class CanvasRef(Reference):\n    type: Optional[constr(regex=r'^Canvas$')] = None\n",
 #       "after": "\n\nModel.update_forward_refs()",
 #       "data": "\n\nclass RangeRef(Reference):\n    type: Optional[constr(regex=r'^Range$')] = None\n"
 #   }
]


def process_change(skeleton, change):
    print(f"Processing change: {change['description']} (Type: {change['type']})")

    if change["type"] == "replace":
        needle = skeleton.find(change["find"])
        if needle == -1:
            print("Needle not found - skipping change")
        else:
            skeleton = skeleton.replace(change["find"], change["replace"])

    if change["type"] == "insert":
        start = skeleton.find(change["before"])
        after = skeleton.find(change["after"])
        if start == -1:
            print("Before string not found - skipping change")
        else:
            if after == -1:
                print("After string not found - skipping change")
            else:
                skeleton = skeleton[:start + len(change["before"])] + change["data"] + skeleton[after:]

    return skeleton


def modify_skeleton(skeleton_file):
    print("Opening Skeleton file...")
    skeleton = open(skeleton_file).read()

    print(f"Processing {len(CHANGES)} changes")
    for change in CHANGES:
        skeleton = process_change(skeleton, change)

    print("Changes processed, writing out fixed Skeleton")
    with open(skeleton_file, "w") as out:
        out.write(skeleton)

def modify_schema(schema_filename):
    with open(schema_filename, 'r') as file:
        schema = json.load(file)

    # Remove:
    # "anyOf":[
    #   { "required": ["width"] },
    #   { "required": ["height"] },
    #   { "required": ["duration"] }
    # ],
    # "dependencies": {
    #   "width": ["height"],
    #   "height": ["width"]
    # }
    # In canvas, placeholderCanvas and accompanyingCanvas
    # classes

    locations = ["canvas", "placeholderCanvas", "accompanyingCanvas"]
    for location in locations:
        container = schema["classes"][location]
        for item in container["allOf"]:
            if "properties" in item:
                item.pop("anyOf")
                item.pop("dependencies")


    with open(schema_filename, 'w') as f:
        json.dump(schema, f, indent=4)    

if __name__ == "__main__":
    print("== Prezi3 Skeleton Fixer ==")
    safety = input("WARNING: This will overwrite the existing Skeleton in-place. Continue y/n? ")

    if safety.lower() != "y":
        exit()

    modify_skeleton()
    print("Done!")
