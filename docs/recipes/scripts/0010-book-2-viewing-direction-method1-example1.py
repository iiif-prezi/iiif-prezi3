from iiif_prezi3 import Manifest, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
base_url = "https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction"

manifest = Manifest(id=f"{base_url}/manifest-rtl.json",
                    label="Book with Right-to-Left Viewing Direction",
                    summary="Playbill for \"Akiba gongen kaisen-banashi,\" \"Futatsu chōchō kuruwa nikki\" and \"Godairiki koi no fūjime\" performed at the Chikugo Theater in Osaka from the fifth month of Kaei 2 (May, 1849); main actors: Gadō Kataoka II, Ebizō Ichikawa VI, Kitō Sawamura II, Daigorō Mimasu IV and Karoku Nakamura I; on front cover: producer Mominosuke Ichikawa's crest.",
                    viewingDirection="right-to-left")

canvas1 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/4f92cceb12dd53b52433425ce44308c7-ucla_bib1987273_no001_rs_001",
                                         id=f"{base_url}/canvas/p1",
                                         label="front cover",
                                         anno_id=f"{base_url}/annotation/p0001-image",
                                         anno_page_id=f"{base_url}/page/p1/1")

canvas2 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/4f92cceb12dd53b52433425ce44308c7-ucla_bib1987273_no001_rs_002",
                                         id=f"{base_url}/canvas/p2",
                                         label="pages 1–2",
                                         anno_id=f"{base_url}/annotation/p0002-image",
                                         anno_page_id=f"{base_url}/page/p2/1")

canvas3 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/4f92cceb12dd53b52433425ce44308c7-ucla_bib1987273_no001_rs_003",
                                         id=f"{base_url}/canvas/p3",
                                         label="pages 3–4",
                                         anno_id=f"{base_url}/annotation/p0003-image",
                                         anno_page_id=f"{base_url}/page/p3/1")

canvas4 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/4f92cceb12dd53b52433425ce44308c7-ucla_bib1987273_no001_rs_004",
                                         id=f"{base_url}/canvas/p4",
                                         label="pages 5–6",
                                         anno_id=f"{base_url}/annotation/p0004-image",
                                         anno_page_id=f"{base_url}/page/p4/1")

canvas5 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/4f92cceb12dd53b52433425ce44308c7-ucla_bib1987273_no001_rs_005",
                                         id=f"{base_url}/canvas/p5",
                                         label="back cover",
                                         anno_id=f"{base_url}/annotation/p0005-image",
                                         anno_page_id=f"{base_url}/page/p5/1")

print(manifest.json(indent=2))
