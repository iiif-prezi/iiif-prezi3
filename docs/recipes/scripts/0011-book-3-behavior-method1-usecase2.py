from iiif_prezi3 import Manifest, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
manifest = Manifest(id="https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/manifest-individuals.json",
                    label={"ca": ["[Conoximent de las orines] Ihesus, Ihesus. En nom de Deu et dela beneyeta sa mare e de tots los angels i archangels e de tots los sants e santes de paradis yo micer Johannes comense aquest libre de reseptes en l’ayn Mi 466."]},
                    behavior=["individuals"])

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
