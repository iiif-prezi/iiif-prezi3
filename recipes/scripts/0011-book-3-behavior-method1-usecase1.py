from iiif_prezi3 import Manifest, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
manifest = Manifest(id="https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/manifest-continuous.json",
                    label={"gez": ["Ms. 21 Māzemurā Dāwit, Asmat [መዝሙረ ዳዊት]"]},
                    behavior=["continuous"])
canvas1 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/8c169124171e6b2253b698a22a938f07-21198-zz001hbmd9_1300412_master",
                                         id="https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/canvas/s1",
                                         label="Section 1 [Recto]",
                                         anno_id="https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/annotation/s0001-image",
                                         anno_page_id="https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/page/s1/1")

canvas2 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/8c169124171e6b2253b698a22a938f07-21198-zz001hbmft_1300418_master",
                                         id="https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/canvas/s2",
                                         label="Section 2 [Recto]",
                                         anno_id="https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/annotation/s0002-image",
                                         anno_page_id="https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/page/s2/1")

canvas3 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/8c169124171e6b2253b698a22a938f07-21198-zz001hbmgb_1300426_master",
                                         id="https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/canvas/s3",
                                         label="Section 3 [Recto]",
                                         anno_id="https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/annotation/s0003-image",
                                         anno_page_id="https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/page/s3/1")

canvas4 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/8c169124171e6b2253b698a22a938f07-21198-zz001hbmhv_1300436_master",
                                         id="https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/canvas/s4",
                                         label="Section 4 [Recto]",
                                         anno_id="https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/annotation/s0004-image",
                                         anno_page_id="https://iiif.io/api/cookbook/recipe/0011-book-3-behavior/page/s4/1")

print(manifest.json(indent=2))
