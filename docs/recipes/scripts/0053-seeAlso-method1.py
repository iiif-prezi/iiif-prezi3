from iiif_prezi3 import Manifest, LinkedResource, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
base_url = "https://iiif.io/api/cookbook/recipe/0053-seeAlso"
image_base = "https://iiif.io/api/image/3.0/example/reference/4f92cceb12dd53b52433425ce44308c7-ucla_bib1987273_no001_rs"

linked_resource = LinkedResource(
    id="https://fixtures.iiif.io/other/UCLA/ezukushi_mods.xml",
    type="Dataset",
    label="MODS metadata",
    format="text/xml",
    profile="http://www.loc.gov/mods/v3",
)
manifest = Manifest(
    id=f"{base_url}/manifest.json",
    label="Linking to Structured Metadata",
    summary="Playbill for \"Akiba gongen kaisen-banashi,\" \"Futatsu chōchō kuruwa nikki\" and \"Godairiki koi no fūjime\" performed at the Chikugo Theater in Osaka from the fifth month of Kaei 2 (May, 1849); main actors: Gadō Kataoka II, Ebizō Ichikawa VI, Kitō Sawamura II, Daigorō Mimasu IV and Karoku Nakamura I; on front cover: producer Mominosuke Ichikawa's crest.",
    viewingDirection="right-to-left",
    seeAlso=linked_resource,
)

canvas_data = [
    ("p1", "front cover", "001", "p0001"),
    ("p2", "pages 1\u20132", "002", "p0002"),
    ("p3", "pages 3\u20134", "003", "p0003"),
    ("p4", "pages 5\u20136", "004", "p0004"),
    ("p5", "back cover", "005", "p0005"),
]

for canvas_id, label, image_num, anno_num in canvas_data:
    manifest.make_canvas_from_iiif(
        url=f"{image_base}_{image_num}",
        id=f"{base_url}/canvas/{canvas_id}",
        label=label,
        anno_id=f"{base_url}/annotation/{anno_num}-image",
        anno_page_id=f"{base_url}/page/{canvas_id}/1",
    )

print(manifest.json(indent=2))
