import json


def load_extensions_from_json():
    try:
        extensions = json.load(open("extensions.json"))
    except FileNotFoundError:
        return

    for ext in extensions:
        __import__(f"iiif_prezi3.extensions.{ext}")


def load_extension(path):
    pass


def monkeypatch_schema(schema_class, patch_classes):
    schema_bases = list(schema_class.__bases__)
    if type(patch_classes) == list:
        for c in patch_classes:
            schema_bases.append(c)
    else:
        schema_bases.append(patch_classes)
    schema_class.__bases__ = tuple(schema_bases)
