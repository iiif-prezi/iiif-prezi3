# Book 'behavior' Variations (continuous, individuals)
### Recipe: [https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/](https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/)
### JSON-LD Use Case 1: [https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/manifest-continuous.json](https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/manifest-continuous.json)
### JSON-LD Use Case 2: [https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/manifest-individuals.json](https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/manifest-individuals.json)

## Method 1 - Setting the `behaviour` property during object construction
### Use Case 1
```python
from iiif_prezi3 import Manifest, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
manifest = Manifest(id="https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/manifest-continuous.json",
                    label={"gez": ["Ms. 21 Māzemurā Dāwit, Asmat [መዝሙረ ዳዊት]"]},
                    behaviour=["continuous"])
canvas1 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/8c169124171e6b2253b698a22a938f07-21198-zz001hbmd9_1300412_master",
                                         id="https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/canvas/s1",
                                         label="Section 1 [Recto]")
canvas1.items[0].id = "https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/page/s1/1"
canvas1.items[0].items[0].id = "https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/annotation/s0001-image"

canvas2 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/8c169124171e6b2253b698a22a938f07-21198-zz001hbmft_1300418_master",
                                         id="https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/canvas/s2",
                                         label="Section 2 [Recto]")
canvas2.items[0].id = "https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/page/s2/1"
canvas2.items[0].items[0].id = "https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/annotation/s0002-image"

canvas3 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/8c169124171e6b2253b698a22a938f07-21198-zz001hbmgb_1300426_master",
                                         id="https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/canvas/s3",
                                         label="Section 3 [Recto]")
canvas3.items[0].id = "https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/page/s3/1"
canvas3.items[0].items[0].id = "https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/annotation/s0003-image"

canvas4 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/8c169124171e6b2253b698a22a938f07-21198-zz001hbmhv_1300436_master",
                                         id="https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/canvas/s4",
                                         label="Section 4 [Recto]")
canvas4.items[0].id = "https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/page/s4/1"
canvas4.items[0].items[0].id = "https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/annotation/s0004-image"

print(manifest.json(indent=2))
```

### Use Case 2
```python
from iiif_prezi3 import Manifest, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
manifest = Manifest(id="https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/manifest-individuals.json",
                    label={"ca": ["[Conoximent de las orines] Ihesus, Ihesus. En nom de Deu et dela beneyeta sa mare e de tots los angels i archangels e de tots los sants e santes de paradis yo micer Johannes comense aquest libre de reseptes en l’ayn Mi 466."]},
                    behaviour=["individuals"])

canvas1 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/85a96c630f077e6ac6cb984f1b752bbf-0-21198-zz00022840-1-master",
                                         id="https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/canvas/v1",
                                         label="inside cover; 1r")
canvas1.items[0].id = "https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/page/v1/1"
canvas1.items[0].items[0].id = "https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/annotation/v0001-image"

canvas2 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/85a96c630f077e6ac6cb984f1b752bbf-1-21198-zz00022882-1-master",
                                         id="https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/canvas/v2",
                                         label="2v, 3r")
canvas2.items[0].id = "https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/page/v2/1"
canvas2.items[0].items[0].id = "https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/annotation/v0002-image"

canvas3 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/85a96c630f077e6ac6cb984f1b752bbf-2-21198-zz000228b3-1-master",
                                         id="https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/canvas/v3",
                                         label="3v, 4r")
canvas3.items[0].id = "https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/page/v3/1"
canvas3.items[0].items[0].id = "https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/annotation/v0003-image"

canvas4 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/85a96c630f077e6ac6cb984f1b752bbf-3-21198-zz000228d4-1-master",
                                         id="https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/canvas/v4",
                                         label="4v, 5r")
canvas4.items[0].id = "https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/page/v4/1"
canvas4.items[0].items[0].id = "https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/annotation/v0004-image"

print(manifest.json(indent=2))
```