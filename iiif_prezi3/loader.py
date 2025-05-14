import json
import os


def load_bundled_extensions(extensions=None):

    extensions_to_load = []

    if extensions and isinstance(extensions, list):
        extensions_to_load = extensions
    elif not extensions or (extensions and not isinstance(extensions, str)):
        if not extensions:
            extension_file = os.path.join(os.path.dirname(__file__), 'config', 'extensions.json')
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


def monkeypatch_schema(schema_classes, patch_classes):
    if isinstance(schema_classes, list):
        for schema_class in schema_classes:
            schema_bases = list(schema_class.__bases__)
            if isinstance(patch_classes, list):
                for c in patch_classes:
                    schema_bases.append(c)
            else:
                schema_bases.append(patch_classes)
            schema_class.__bases__ = tuple(schema_bases)
    else:
        schema_bases = list(schema_classes.__bases__)
        if isinstance(patch_classes, list):
            for c in patch_classes:
                schema_bases.append(c)
        else:
            schema_bases.append(patch_classes)
        schema_classes.__bases__ = tuple(schema_bases)
