from iiif_prezi3 import Manifest, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
base_url = "https://iiif.io/api/cookbook/recipe/0030-multi-volume"

image_base = "https://iiif.io/api/image/3.0/example/reference/5b0b39c2bf5591d21d807f9aadb437fa-uclaeal_wahon_A06_bib1974505_vol01"

manifest = Manifest(
    id=f"{base_url}/manifest_v1.json",
    label="Seirō ehon nenjū gyōji : kan 1 | 青楼絵本年中行事 : 巻 1",
    behavior="individuals",
    viewingDirection="right-to-left",
)

canvas_data = [
    ("p1", "Front cover", "001", "p0001"),
    ("p2", "Page spread 1", "002", "p0002"),
    ("p3", "Page spread 2", "003", "p0003"),
    ("p4", "Page spread 3", "007", "p0004"),
    ("p5", "Page spread 4", "008", "p0005"),
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
