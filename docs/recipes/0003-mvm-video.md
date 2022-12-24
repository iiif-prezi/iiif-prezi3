# Simplest Manifest - Video
|              | **Cookbook URLs**                                                                                                                    |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------|
| **Recipe:**  | [https://iiif.io/api/cookbook/recipe/0003-mvm-video/](https://iiif.io/api/cookbook/recipe/0003-mvm-video/)                           |
| **JSON-LD:** | [https://iiif.io/api/cookbook/recipe/0003-mvm-video/manifest.json](https://iiif.io/api/cookbook/recipe/0003-mvm-video/manifest.json) |

### Method 1 - Building the structure manually and using the `add_item` helper
```python
from iiif_prezi3 import Manifest, AnnotationPage, Annotation, ResourceItem, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"

manifest = Manifest(id="https://iiif.io/api/cookbook/recipe/0003-mvm-video/manifest.json", label="Video Example 3")
canvas = manifest.make_canvas(id="https://iiif.io/api/cookbook/recipe/0003-mvm-video/canvas")
anno_body = ResourceItem(id="https://fixtures.iiif.io/video/indiana/lunchroom_manners/high/lunchroom_manners_1024kb.mp4",
                    type="Video",
                    format="video/mp4")
anno_page = AnnotationPage(id="https://iiif.io/api/cookbook/recipe/0003-mvm-video/canvas/page")
anno = Annotation(id="https://iiif.io/api/cookbook/recipe/0003-mvm-video/canvas/page/annotation",
                  motivation="painting",
                  body=anno_body,
                  target=canvas.id)

hwd = {"height": 360, "width": 480, "duration": 572.034}
anno_body.set_hwd(**hwd)
canvas.set_hwd(**hwd)

anno_page.add_item(anno)
canvas.add_item(anno_page)

print(manifest.json(indent=2))
```
