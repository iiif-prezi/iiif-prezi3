CHANGES = [
    {
        "description": "Fix LngString's missing __root__",
        "type": "replace",
        "find": "class LngString(Base):\n    pass",
        "replace": "class LngString(Base):\n    __root__: Dict[str, List[str]]"
    },
    {
        "description": "Rename v2 Service properties so they are not private",
        "type": "replace",
        "find": "class ServiceItem1(Base):\n    _id: Id = Field(..., alias='@id')\n    _type: str = Field(..., alias='@type')",
        "replace": "class ServiceItem1(Base):\n    id: Id = Field(..., alias='@id')\n    type: str = Field(..., alias='@type')"
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
                skeleton = skeleton[:start+len(change["before"])] + change["data"] + skeleton[after:]

    return skeleton


def modify_skeleton():
    print("Opening Skeleton file...")
    skeleton = open("../iiif_prezi3/skeleton.py").read()

    print(f"Processing {len(CHANGES)} changes")
    for change in CHANGES:
        skeleton = process_change(skeleton, change)

    print("Changes processed, writing out fixed Skeleton")
    with open("../iiif_prezi3/skeleton.py", "w") as out:
        out.write(skeleton)


if __name__ == "__main__":
    print("== Prezi3 Skeleton Fixer ==")
    safety = input("WARNING: This will overwrite the existing Skeleton in-place. Continue y/n? ")

    if safety.lower() != "y":
        exit()

    modify_skeleton()
    print("Done!")
