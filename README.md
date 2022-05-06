# iiif-prezi3
IIIF Presentation API 3 Python Library

## Installation
### PyPi
The easiest way to install the `iiif-prezi3` library is directly from PyPi:

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
```
>>> import iiif_prezi3
>>> iiif_prezi3.__version__
'0.0.2.1'
```

### Directly creating a Manifest
```
>>> from iiif_prezi3 import Manifest
>>> m = Manifest(id="https://example.com/iiif/manifest.json", type="Manifest", label={"en":["Example Manifest"]})
>>> print(m.json(exclude_unset=True, indent=2))
{
  "id": "https://example.com/iiif/manifest.json",
  "type": "Manifest",
  "label": {}
}
```
### Importing an existing IIIF Manifest
If you have an existing IIIF Presentation v3 Manifest, you can load it via the built-in `json` module and create the objects:
```
>>> from iiif_prezi3 import Manifest
>>> import json
>>> manifest_json = json.load(open("example.json"))
>>> m = Manifest(**manifest_json)
>>> print(m.json(exclude_unset=True, indent=2))
{
  "id": "https://iiif.io/api/cookbook/recipe/0003-mvm-video/manifest.json",
  "type": "Manifest",
  "label": {},
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

Called without argument, this method will load all bundled extensions listed in the [iiif_prezi3/config/extensions.json](iiif_prezi3/config/extensions.json) file. If you wish to only load selected extensions from those available bundled with the library, you can pass either the path to a JSON file, or a list of extension names as an argument to the function:
```
>>> import iiif_prezi3
>>> iiif_prezi3.load_bundled_extensions(extensions="/path/to/chosen_extensions.json")
```
```
>>> import iiif_prezi3
>>> iiif_prezi3.load_bundled_extensions(extensions=['example_extension'])
```

## Running Tests
Tests (including linting) can be run using [tox](https://tox.wiki/en/latest/). First, install tox with `pip install tox`, then type `tox`.
