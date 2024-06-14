from iiif_prezi3 import Manifest, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
base_url = "https://iiif.io/api/cookbook/recipe/0009-book-1"

manifest = Manifest(id=f"{base_url}/manifest.json",
                    label="Simple Manifest - Book",
                    behavior=["paged"])
canvas1 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/59d09e6773341f28ea166e9f3c1e674f-gallica_ark_12148_bpt6k1526005v_f18",
                                         id=f"{base_url}/canvas/p1",
                                         label="Blank page",
                                         anno_id=f"{base_url}/annotation/p0001-image",
                                         anno_page_id=f"{base_url}/page/p1/1")

canvas2 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/59d09e6773341f28ea166e9f3c1e674f-gallica_ark_12148_bpt6k1526005v_f19",
                                         id=f"{base_url}/canvas/p2",
                                         label="Frontispiece",
                                         anno_id=f"{base_url}/annotation/p0002-image",
                                         anno_page_id=f"{base_url}/page/p2/1")

canvas3 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/59d09e6773341f28ea166e9f3c1e674f-gallica_ark_12148_bpt6k1526005v_f20",
                                         id=f"{base_url}/canvas/p3",
                                         label="Title page",
                                         anno_id=f"{base_url}/annotation/p0003-image",
                                         anno_page_id=f"{base_url}/page/p3/1")

canvas4 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/59d09e6773341f28ea166e9f3c1e674f-gallica_ark_12148_bpt6k1526005v_f21",
                                         id=f"{base_url}/canvas/p4",
                                         label="Blank page",
                                         anno_id=f"{base_url}/annotation/p0004-image",
                                         anno_page_id=f"{base_url}/page/p4/1")

canvas5 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/59d09e6773341f28ea166e9f3c1e674f-gallica_ark_12148_bpt6k1526005v_f22",
                                         id=f"{base_url}/canvas/p5",
                                         label="Bookplate",
                                         anno_id=f"{base_url}/annotation/p0005-image",
                                         anno_page_id=f"{base_url}/page/p5/1")

print(manifest.json(indent=2))
