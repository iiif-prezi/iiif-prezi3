from iiif_prezi3 import Manifest, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
base_url = "https://iiif.io/api/cookbook/recipe/0202-start-canvas"
image_base = "https://iiif.io/api/image/3.0/example/reference/59d09e6773341f28ea166e9f3c1e674f-gallica_ark_12148_bpt6k1526005v"

canvases = [
    {"page": "p1", "num": "0001", "folio": "f18", "label": "Blank page"},
    {"page": "p2", "num": "0002", "folio": "f19", "label": "Frontispiece"},
    {"page": "p3", "num": "0003", "folio": "f20", "label": "Title page"},
    {"page": "p4", "num": "0004", "folio": "f21", "label": "Blank page"},
    {"page": "p5", "num": "0005", "folio": "f22", "label": "Bookplate"},
]

manifest = Manifest(
    id=f"{base_url}/manifest.json",
    label="Multiple Related Images (Book, etc.)",
    start={"id": f"{base_url}/canvas/p2", "type": "Canvas"},
)

for c in canvases:
    manifest.make_canvas_from_iiif(
        url=f"{image_base}_{c['folio']}",
        id=f"{base_url}/canvas/{c['page']}",
        label=c["label"],
        anno_id=f"{base_url}/annotation/p{c['num']}-image",
        anno_page_id=f"{base_url}/page/{c['page']}/1",
    )

print(manifest.json(indent=2))
