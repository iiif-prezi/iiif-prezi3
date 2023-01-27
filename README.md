# iiif-prezi3
IIIF Presentation API 3 Python Library

[![PyPI version](https://badge.fury.io/py/iiif-prezi3.svg)](https://badge.fury.io/py/iiif-prezi3)
![PyPI — Python versions](https://img.shields.io/pypi/pyversions/iiif-prezi3)
![PyPI - License](https://img.shields.io/pypi/l/iiif-prezi3)
[![CI](https://github.com/iiif-prezi/iiif-prezi3/actions/workflows/ci.yml/badge.svg)](https://github.com/iiif-prezi/iiif-prezi3/actions/workflows/ci.yml)

## Installation
### PyPI
The easiest way to install the `iiif-prezi3` library is directly from PyPI:

```
pip install iiif-prezi3
```
### Manual installation
Alternatively, you can clone the repository and run `setup.py` locally:
```
git clone https://github.com/iiif-prezi/iiif-prezi3.git
```
or
```
git clone git@github.com:iiif-prezi/iiif-prezi3.git
```
followed by:
```
cd iiif-prezi3
python setup.py install
```

## Basic Usage
You can now import the library or individual classes from within Python and start creating your IIIF Presentation 3 objects:

### Directly creating a Manifest
```
>>> from iiif_prezi3 import Manifest
>>> m = Manifest(id="https://example.com/iiif/manifest.json", label={"en":["Example Manifest"]})
>>> print(m.json(indent=2))
{
  "@context": "http://iiif.io/api/presentation/3/context.json",
  "id": "https://example.com/iiif/manifest.json",
  "type": "Manifest",
  "label": {
    "en": [
      "Example Manifest"
    ]
  }
}
```
### Importing an existing IIIF Manifest
If you have an existing IIIF Presentation v3 Manifest, you can load it via the built-in `json` module and create the objects:
```
>>> from iiif_prezi3 import Manifest
>>> import json
>>> manifest_json = json.load(open("example.json"))
>>> m = Manifest(**manifest_json)
>>> print(m.json(indent=2))
{
  "@context": "http://iiif.io/api/presentation/3/context.json",
  "id": "https://iiif.io/api/cookbook/recipe/0003-mvm-video/manifest.json",
  "type": "Manifest",
  "label": {
    "en": [
      "Video Example 3"
    ]
  },
  "items": [
    {
      "id": "https://iiif.io/api/cookbook/recipe/0003-mvm-video/canvas",
      "type": "Canvas",
      "height": 360,
      "width": 640,
      "duration": 572.034,
      "items": [
        {
          "id": "https://iiif.io/api/cookbook/recipe/0003-mvm-video/canvas/page",
          "type": "AnnotationPage",
          "items": [
            {
              "id": "https://iiif.io/api/cookbook/recipe/0003-mvm-video/canvas/page/annotation",
              "type": "Annotation",
              "motivation": "painting",
              "body": {
                "id": "https://fixtures.iiif.io/video/indiana/lunchroom_manners/high/lunchroom_manners_1024kb.mp4",
                "type": "Video",
                "height": 360,
                "width": 480,
                "duration": 572.034,
                "format": "video/mp4"
              },
              "target": "https://iiif.io/api/cookbook/recipe/0003-mvm-video/canvas"
            }
          ]
        }
      ]
    }
  ]
}
```

## Extensions
`iiif-prezi3` includes the capability to load extensions to the IIIF Presentation schema (e.g [navPlace](https://iiif.io/api/extension/navplace/)) and modify the library's Python classes to include extra properties, validation, helper methods, etc.

Published extensions from the [IIIF Registry of Extensions](https://iiif.io/api/extension/) are included with the package, and can be loaded using the `iiif_prezi3.load_bundled_extensions()` method.

Called without argument, this method will load all bundled extensions listed in the  [iiif_prezi3/config/extensions.json](https://github.com/iiif-prezi/iiif-prezi3/blob/main/iiif_prezi3/config/extensions.json) file. If you wish to only load selected extensions from those available bundled with the library, you can pass either the path to a JSON file, or a list of extension names as an argument to the function:
```
>>> import iiif_prezi3
>>> iiif_prezi3.load_bundled_extensions(extensions="/path/to/chosen_extensions.json")
```
```
>>> import iiif_prezi3
>>> iiif_prezi3.load_bundled_extensions(extensions=['example_extension'])
```

Extensions work in much the same way as helper methods, and are monkeypatched into the relevant objects in the `iiif_prezi3.skeleton` class, from which everything is loaded.
For a simple example, please see the `extensions/example_extension.py` file, and the [documentation on writing a helper method](https://github.com/iiif-prezi/iiif-prezi3/blob/main/docs/write-helper-method.md).
## Local Development
For developing `iiif-prezi3` locally, clone the repo and then install it and the development dependencies using pip's "editable mode":
```bash
git clone git@github.com:iiif-prezi/iiif-prezi3.git
cd iiif-prezi3
pip install -e .[dev]
```
## Running Tests
Tests (including linting) can be run using [tox](https://tox.wiki/en/latest/). First, install tox with `pip install tox`, then type `tox`.

## Versioning
`iiif-prezi3` broadly follows [Semantic Versioning](https://semver.org/). Patch releases are used for bug fixes, minor releases add new functionality and maintain backwards compatibility, and major versions contain breaking changes to the public API of the library. Links to the changes between individual versions can be found on the [releases](https://github.com/iiif-prezi/iiif-prezi3/releases) page.

## Get Involved
The `iiif-prezi3` maintainers welcome contributions from the community - issues, pull requests, use cases, etc. We have a [guideline document for contributions](https://github.com/iiif-prezi/iiif-prezi3/blob/main/CONTRIBUTING.md) and a channel `#iiif-prezi3` on the IIIF Slack workspace, which can be joined from the [IIIF website's Get Involved page](https://iiif.io/get-involved/).
