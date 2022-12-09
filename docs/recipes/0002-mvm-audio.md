# Simplest Manifest - Audio
### Recipe: [https://iiif.io/api/cookbook/recipe/0002-mvm-audio/](https://iiif.io/api/cookbook/recipe/0002-mvm-audio/)
### JSON-LD: [https://iiif.io/api/cookbook/recipe/0002-mvm-audio/manifest.json](https://iiif.io/api/cookbook/recipe/0002-mvm-audio/manifest.json)

## Method 1 - Building the structure and using the `add_item` helper
```python
from iiif_prezi3 import Manifest, AnnotationPage, Annotation, ResourceItem, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"

manifest = Manifest(id="https://iiif.io/api/cookbook/recipe/0002-mvm-audio/manifest.json", label="Simplest Audio Example")
canvas = manifest.make_canvas(id="https://iiif.io/api/cookbook/recipe/0002-mvm-audio/canvas", duration=1985.024)
anno_body = ResourceItem(id="https://fixtures.iiif.io/audio/indiana/mahler-symphony-3/CD1/medium/128Kbps.mp4",
                    type="Sound",
                    format="audio/mp4",
                    duration=1985.024)
anno_page = AnnotationPage(id="https://iiif.io/api/cookbook/recipe/0002-mvm-audio/canvas/page")
anno = Annotation(id="https://iiif.io/api/cookbook/recipe/0002-mvm-audio/canvas/page/annotation",
                  motivation="painting",
                  body=anno_body,
                  target=canvas.id)
anno_page.add_item(anno)
canvas.add_item(anno_page)

print(manifest.json(indent=2))
```
