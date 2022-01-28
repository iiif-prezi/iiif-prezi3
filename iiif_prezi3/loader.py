import json
import os


def load_bundled_extensions(extensions=None):

    extensions_to_load = []

    if extensions and type(extensions) == list:
        extensions_to_load = extensions
    elif not extensions or (extensions and type(extensions) == str):
        if not extensions:
            extension_file =  os.path.join(os.path.dirname(__file__), 'config', 'extensions.json')
        else:
            extension_file = extensions
        try:
            with open(extension_file, 'r') as extension_data:
                extensions_to_load = json.load(extension_data)
        except FileNotFoundError:
            # TODO: Add a log error here
            return

    for ext in extensions_to_load:
        load_extension(f"iiif_prezi3.extensions.{ext}")


def load_extension(path):
    try:
        __import__(path)
    except ModuleNotFoundError:
        # TODO: Add a log error here
        return


def monkeypatch_schema(schema_class, patch_classes):
    schema_bases = list(schema_class.__bases__)
    if type(patch_classes) == list:
        for c in patch_classes:
            schema_bases.append(c)
    else:
        schema_bases.append(patch_classes)
    schema_class.__bases__ = tuple(schema_bases)
