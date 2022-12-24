from iiif_prezi3 import Manifest, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"

manifest = Manifest(id="https://iiif.io/api/cookbook/recipe/0009-book-1/manifest.json",
                    label="Simple Manifest - Book",
                    behavior=["paged"])
canvas1 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/59d09e6773341f28ea166e9f3c1e674f-gallica_ark_12148_bpt6k1526005v_f18",
                                         id="https://iiif.io/api/cookbook/recipe/0009-book-1/canvas/p1",
                                         label="Blank page")
canvas1.items[0].id = "https://iiif.io/api/cookbook/recipe/0009-book-1/page/p1/1"
canvas1.items[0].items[0].id = "https://iiif.io/api/cookbook/recipe/0009-book-1/annotation/p0001-image"

canvas2 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/59d09e6773341f28ea166e9f3c1e674f-gallica_ark_12148_bpt6k1526005v_f19",
                                         id="https://iiif.io/api/cookbook/recipe/0009-book-1/canvas/p2",
                                         label="Frontispiece")
canvas2.items[0].id = "https://iiif.io/api/cookbook/recipe/0009-book-1/page/p2/1"
canvas2.items[0].items[0].id = "https://iiif.io/api/cookbook/recipe/0009-book-1/annotation/p0002-image"

canvas3 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/59d09e6773341f28ea166e9f3c1e674f-gallica_ark_12148_bpt6k1526005v_f20",
                                         id="https://iiif.io/api/cookbook/recipe/0009-book-1/canvas/p3",
                                         label="Title page")
canvas3.items[0].id = "https://iiif.io/api/cookbook/recipe/0009-book-1/page/p3/1"
canvas3.items[0].items[0].id = "https://iiif.io/api/cookbook/recipe/0009-book-1/annotation/p0003-image"

canvas4 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/59d09e6773341f28ea166e9f3c1e674f-gallica_ark_12148_bpt6k1526005v_f21",
                                         id="https://iiif.io/api/cookbook/recipe/0009-book-1/canvas/p4",
                                         label="Blank page")
canvas4.items[0].id = "https://iiif.io/api/cookbook/recipe/0009-book-1/page/p4/1"
canvas4.items[0].items[0].id = "https://iiif.io/api/cookbook/recipe/0009-book-1/annotation/p0004-image"

canvas5 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/59d09e6773341f28ea166e9f3c1e674f-gallica_ark_12148_bpt6k1526005v_f22",
                                         id="https://iiif.io/api/cookbook/recipe/0009-book-1/canvas/p5",
                                         label="Bookplate")
canvas5.items[0].id = "https://iiif.io/api/cookbook/recipe/0009-book-1/page/p5/1"
canvas5.items[0].items[0].id = "https://iiif.io/api/cookbook/recipe/0009-book-1/annotation/p0005-image"

print(manifest.json(indent=2))
