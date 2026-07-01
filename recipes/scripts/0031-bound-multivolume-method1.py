import unicodedata

from iiif_prezi3 import Manifest, CanvasRef, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "de"
base_url = "https://iiif.io/api/cookbook/recipe/0031-bound-multivolume"
image_base = "https://iiif.io/api/image/3.0/example/reference/15f769d62ca9a3a2deca390efed75d73"

def normalize_nfd_unicode(s):
    return unicodedata.normalize('NFD', s)

manifest = Manifest(
    id=f"{base_url}/manifest.json",
    label=normalize_nfd_unicode("Gottesdienstliche Ceremonien, Oder H. Kirchen-Gebräuche Und Religions-Pflichten Der Christen"),
)

canvases = [
    ("p1", "Front cover",               "1_frontcover",          "p0001"),
    ("p2", "Inside front cover",        "2_insidefrontcover",    "p0002"),
    ("p3", "Vol. 1 title page",         "3_titlepage1",          "p0003"),
    ("p4", "Vol. 1 title page (verso)", "4_titlepage1_verso",    "p0004"),
    ("p5", "Vol. 2 title page",         "5_titlepage2",          "p0005"),
    ("p6", "Vol. 2 title page (verso)", "6_titlepage2_verso",    "p0006"),
]

for canvas_id, label, image_id, anno_num in canvases:
    manifest.make_canvas_from_iiif(
        url=f"{image_base}-{image_id}",
        id=f"{base_url}/canvas/{canvas_id}",
        label={"en": [label]},
        anno_id=f"{base_url}/annotation/{anno_num}-image",
        anno_page_id=f"{base_url}/page/{canvas_id}/1",
    )

toc = manifest.make_range(
    id=f"{base_url}/range/r0",
    label=normalize_nfd_unicode("Gottesdienstliche Ceremonien, Oder H. Kirchen-Gebräuche Und Religions-Pflichten Der Christen"),
)

r1 = toc.make_range(id=f"{base_url}/range/r1")
r1.add_label("Front Matter", "en")
r1.add_item(CanvasRef(id=f"{base_url}/canvas/p1", type="Canvas"))
r1.add_item(CanvasRef(id=f"{base_url}/canvas/p2", type="Canvas"))

r2 = toc.make_range(
    id=f"{base_url}/range/r2",
    label="Erste Ausgabe. Begreift die Ceremonien der Lutheraner von der Augspurgischen Confession, der Reformirten, der Holländischen u. a. Kirchen",
)
r2.add_item(CanvasRef(id=f"{base_url}/canvas/p3", type="Canvas"))
r2.add_item(CanvasRef(id=f"{base_url}/canvas/p4", type="Canvas"))

r3 = toc.make_range(
    id=f"{base_url}/range/r3",
    label="Zweyte Ausgabe. Begreift die Ceremonien der Engl. hohen Kirche : Der Quacker, der Anabaptisten, der Adamiten, der Flagellanten, der Frey-Maurer, der Rhinsbürger...",
)
r3.add_item(CanvasRef(id=f"{base_url}/canvas/p5", type="Canvas"))
r3.add_item(CanvasRef(id=f"{base_url}/canvas/p6", type="Canvas"))

print(manifest.json(indent=2))
