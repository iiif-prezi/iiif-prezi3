# Simple Annotation — Tagging
|              | **Cookbook URLs**                                                                                                                |
|--------------|----------------------------------------------------------------------------------------------------------------------------------|
| **Recipe:**  | [https://iiif.io/api/cookbook/recipe/0021-tagging/](https://iiif.io/api/cookbook/recipe/0021-tagging/)                           |
| **JSON-LD:** | [https://iiif.io/api/cookbook/recipe/0021-tagging/manifest.json](https://iiif.io/api/cookbook/recipe/0021-tagging/manifest.json) |

### Method 1 - Construct an Annotation using the `make_annotation` helper and a dictionary of the `body` properties
```python
from iiif_prezi3 import Manifest

manifest = Manifest(id="https://iiif.io/api/cookbook/recipe/0021-tagging/manifest.json",
                    label={"en": ["Picture of Göttingen taken during the 2019 IIIF Conference"]})
canvas = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/918ecd18c2592080851777620de9bcb5-gottingen",
                               id="https://iiif.io/api/cookbook/recipe/0021-tagging/canvas/p1")
canvas.items[0].id = "https://iiif.io/api/cookbook/recipe/0021-tagging/page/p1/1"
canvas.items[0].items[0].id = "https://iiif.io/api/cookbook/recipe/0021-tagging/annotation/p0001-image"

anno = canvas.make_annotation(id="https://iiif.io/api/cookbook/recipe/0021-tagging/annotation/p0002-ta",
                              motivation="tagging",
                              body= {"type": "TextualBody",
                                     "language": "de",
                                     "format": "text/plain",
                                     "value": "Gänseliesel-Brunnen"},
                              target=canvas.id + "#xywh=265,661,1260,1239")
canvas.annotations[0].id = "https://iiif.io/api/cookbook/recipe/0021-tagging/page/p2/1"

print(manifest.json(indent=2))
```
