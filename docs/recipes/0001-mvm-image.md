# Simplest Manifest - Single Image File
### Recipe: [https://iiif.io/api/cookbook/recipe/0001-mvm-image/](https://iiif.io/api/cookbook/recipe/0001-mvm-image/)
### JSON-LD: [https://iiif.io/api/cookbook/recipe/0001-mvm-image/manifest.json](https://iiif.io/api/cookbook/recipe/0001-mvm-image/manifest.json)

## Method 1 - Using the `make_canvas` and `add_image` helpers
```python
from iiif_prezi3 import Manifest, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"

manifest = Manifest(id="https://iiif.io/api/cookbook/recipe/0001-mvm-image/manifest.json", label="Image 1")
canvas = manifest.make_canvas(id="https://iiif.io/api/cookbook/recipe/0001-mvm-image/canvas/p1", height=1800, width=1200)
anno_page = canvas.add_image(image_url="http://iiif.io/api/presentation/2.1/example/fixtures/resources/page1-full.png",
                             anno_page_id="https://iiif.io/api/cookbook/recipe/0001-mvm-image/page/p1/1",
                             anno_id="https://iiif.io/api/cookbook/recipe/0001-mvm-image/annotation/p0001-image",
                             format="image/png",
                             height=1800,
                             width=1200
                             )

print(manifest.json(indent=2))
```

## Method 2 - Building the structure manually and using the `add_item` helper
```python
from iiif_prezi3 import Manifest, Canvas, AnnotationPage, Annotation, ResourceItem, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"

manifest = Manifest(id="https://iiif.io/api/cookbook/recipe/0001-mvm-image/manifest.json", label="Image 1")
canvas = Canvas(id="https://iiif.io/api/cookbook/recipe/0001-mvm-image/canvas/p1", height=1800, width=1200)
anno_body = ResourceItem(id="http://iiif.io/api/presentation/2.1/example/fixtures/resources/page1-full.png",
                    type="Image",
                    format="image/png",
                    height=1800,
                    width=1200)
anno_page = AnnotationPage(id="https://iiif.io/api/cookbook/recipe/0001-mvm-image/page/p1/1")
anno = Annotation(id="https://iiif.io/api/cookbook/recipe/0001-mvm-image/annotation/p0001-image",
                  motivation="painting",
                  body=anno_body,
                  target=canvas.id)
anno_page.add_item(anno)
canvas.add_item(anno_page)
manifest.add_item(canvas)

print(manifest.json(indent=2))
```

