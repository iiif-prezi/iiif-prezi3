import json

CHANGES = [
    {
        "description": "Fix Annotation model_config",
        "type": "replace",
        "find": "class Annotation(Class):\n    model_config = ConfigDict(extra='allow')\n\n    type:",
        "replace": "class Annotation(Class):\n    model_config = ConfigDict(extra='allow', populate_by_name=True)\n\n    type:"
    },
    {
        "description": "Fix ServiceV3 duplicate model_config",
        "type": "replace",
        "find": "class ServiceV3(Class):\n    model_config = ConfigDict(extra='allow')\n\n    model_config = ConfigDict(\n        extra='allow',\n    )",
        "replace": "class ServiceV3(Class):\n    model_config = ConfigDict(extra='allow', populate_by_name=True)"
    },
    {
        "description": "Fix ServiceV2 duplicate model_config",
        "type": "replace",
        "find": "class ServiceV2(Base):\n    model_config = ConfigDict(extra='allow')\n\n    model_config = ConfigDict(\n        extra='allow',\n    )",
        "replace": "class ServiceV2(Base):\n    model_config = ConfigDict(extra='allow', populate_by_name=True)"
    },
    {
        "description": "Fix Reference duplicate model_config",
        "type": "replace",
        "find": "class Reference(Base):\n    model_config = ConfigDict(extra='allow')\n\n    model_config = ConfigDict(\n        extra='allow',\n    )",
        "replace": "class Reference(Base):\n    model_config = ConfigDict(extra='allow', populate_by_name=True)"
    },
    {
        "description": "Add validation_alias to ServiceV2 fields",
        "type": "replace",
        "find": "    id: Id = Field(..., alias='@id')\n    type: str = Field(..., alias='@type')",
        "replace": "    id: Id = Field(..., alias='@id', validation_alias='id')\n    type: str = Field(..., alias='@type', validation_alias='type')"
    }
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

    # Check if __future__ import is missing and add it
    if "from __future__ import annotations" not in skeleton:
        print("Adding missing __future__ import...")
        # Find the first import line after the header
        import_pos = skeleton.find("from datetime import datetime")
        if import_pos != -1:
            skeleton = skeleton[:import_pos] + "from __future__ import annotations\n\n" + skeleton[import_pos:]

            # Quote ALL forward references in RootModel[Union[...]] patterns
    import re
    print("Quoting forward references in RootModel types...")
    content = re.sub(
        r'RootModel\[Union\[([^\]]+)\]\]',
        lambda m: 'RootModel[Union[' + ', '.join(
            f"'{item.strip()}'" if item.strip() and not item.strip().startswith("'") and item.strip()[0].isupper()
            else item.strip()
            for item in m.group(1).split(',')
        ) + ']]',
        skeleton
    )
    skeleton = content

    print(f"Processing {len(CHANGES)} changes")
    for change in CHANGES:
        skeleton = process_change(skeleton, change)

    print("Changes processed, writing out fixed Skeleton")
    with open(skeleton_file, "w") as out:
        out.write(skeleton)


def modify_schema(schema_filename):
    with open(schema_filename, 'r') as file:
        schema = json.load(file)

        # Remove width/height coupling constraints
    locations = ["canvas", "placeholderCanvas", "accompanyingCanvas"]
    for location in locations:
        container = schema["classes"][location]
        for item in container["allOf"]:
            if "properties" in item:
                item.pop("anyOf", None)
                item.pop("dependencies", None)

                # Remove problematic exclusiveMaximum/exclusiveMinimum that cause datamodel-code-generator errors

    def clean_schema_recursive(obj):
        if isinstance(obj, dict):
            obj.pop("exclusiveMaximum", None)
            obj.pop("exclusiveMinimum", None)
            for value in obj.values():
                clean_schema_recursive(value)
        elif isinstance(obj, list):
            for item in obj:
                clean_schema_recursive(item)

    clean_schema_recursive(schema)

    with open(schema_filename, 'w') as f:
        json.dump(schema, f, indent=4)

if __name__ == "__main__":
    print("== Prezi3 Skeleton Fixer ==")
    safety = input("WARNING: This will overwrite the existing Skeleton in-place. Continue y/n? ")

    if safety.lower() != "y":
        exit()

    modify_skeleton()
    print("Done!")
