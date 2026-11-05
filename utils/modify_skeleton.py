import json

CHANGES = [
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

    # Quote ALL forward references in RootModel[Union[...]] patterns.
    # Base-class subscripts are evaluated at class definition time (the
    # __future__ import doesn't defer them), so unquoted names defined later
    # in the file raise NameError. Allow whitespace/newlines as newer
    # datamodel-codegen versions wrap these across lines; exclude nested
    # brackets so only flat Union[...] lists are rewritten.
    import re
    print("Quoting forward references in RootModel types...")

    def quote_items(m):
        items = [i.strip() for i in m.group(1).split(',') if i.strip()]
        quoted = [f"'{i}'" if i[0].isupper() and not i.startswith("'") else i for i in items]
        return 'RootModel[Union[' + ', '.join(quoted) + ']]'

    skeleton = re.sub(r'RootModel\[\s*Union\[([^\[\]]+)\]\s*\]', quote_items, skeleton)

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
