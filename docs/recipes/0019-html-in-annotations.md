# HTML in Annotations
|              | **Cookbook URLs**                                                                                                                                        |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Recipe:**  | [https://iiif.io/api/cookbook/recipe/0019-html-in-annotations/](https://iiif.io/api/cookbook/recipe/0019-html-in-annotations/)                           |
| **JSON-LD:** | [https://iiif.io/api/cookbook/recipe/0019-html-in-annotations/manifest.json](https://iiif.io/api/cookbook/recipe/0019-html-in-annotations/manifest.json) |

### Method 1 - Construct an Annotation using the `make_annotation` helper and a dictionary of the `body` properties
```python
from iiif_prezi3 import Manifest

manifest = Manifest(id="https://iiif.io/api/cookbook/recipe/0019-html-in-annotations/manifest.json",
                    label={"en": ["Picture of Göttingen taken during the 2019 IIIF Conference"]})
canvas = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/918ecd18c2592080851777620de9bcb5-gottingen",
                               id="https://iiif.io/api/cookbook/recipe/0019-html-in-annotations/canvas-1")
canvas.items[0].id = "https://iiif.io/api/cookbook/recipe/0019-html-in-annotations/canvas-1/annopage-1"
canvas.items[0].items[0].id = "https://iiif.io/api/cookbook/recipe/0019-html-in-annotations/canvas-1/annopage-1/anno-1"

anno = canvas.make_annotation(id="https://iiif.io/api/cookbook/recipe/0019-html-in-annotations/canvas-1/annopage-2/anno-1",
                              motivation="commenting",
                              body= {"type": "TextualBody",
                                     "language": "de",
                                     "format": "text/html",
                                     "value": "<p>Göttinger Marktplatz mit <a href='https://de.wikipedia.org/wiki/G%C3%A4nseliesel-Brunnen_(G%C3%B6ttingen)'>Gänseliesel Brunnen <img src='https://en.wikipedia.org/static/images/project-logos/enwiki.png' alt='Wikipedia logo'></a></p>"},
                              target=canvas.id)
canvas.annotations[0].id = "https://iiif.io/api/cookbook/recipe/0019-html-in-annotations/canvas-1/annopage-2"

print(manifest.json(indent=2))
```
