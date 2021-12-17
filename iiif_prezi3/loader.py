import json
import os


def load_bundled_extensions(extension_file=None):
    if not extension_file:
        extension_file =  os.path.join(os.path.dirname(__file__), 'config', 'extensions.json')
    try:
        extensions = json.load(open(extension_file))
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
