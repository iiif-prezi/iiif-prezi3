from iiif_prezi3 import Manifest, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
base_url = "https://iiif.io/api/cookbook/recipe/0035-foldouts"
image_base = "https://iiif.io/api/image/3.0/example/reference/0a469c27256eda739d43124cc448a3ba"

manifest = Manifest(
    id=f"{base_url}/manifest.json",
    label="Outlines of geology being the substance of a course of lectures "
          "delivered in the Theatre of the Royal Institution in the year 1816",
    behavior="paged",
)

canvas_data = [
    ("1", "Front cover", "1_frontcover", "0001", {}),
    ("2", "Inside front cover", "2_insidefrontcover", "0002", {}),
    ("3", "Foldout, folded", "3_foldout-folded", "0003", {}),
    ("4", "Foldout, unfolded", "4_foldout", "0004", {"behavior": ["non-paged"]}),
    ("5", "Foldout, folded (recto)", "3_foldout-rotated", "0005", {}),
    ("6", "Title page", "5_titlepage", "0006", {}),
    ("7", "Back of title page", "6_titlepage-recto", "0007", {}),
    ("8", "Inside back cover", "8_insidebackcover", "0008", {}),
    ("9", "Back cover", "9_backcover", "0009", {}),
]

for canvas_id, label, image_id, anno_num, extra in canvas_data:
    manifest.make_canvas_from_iiif(
        url=f"{image_base}-{image_id}",
        id=f"{base_url}/canvas/{canvas_id}",
        label=label,
        anno_id=f"{base_url}/annotation/{anno_num}-image",
        anno_page_id=f"{base_url}/page/{canvas_id}/1",
        **extra,
    )

print(manifest.json(indent=2))
