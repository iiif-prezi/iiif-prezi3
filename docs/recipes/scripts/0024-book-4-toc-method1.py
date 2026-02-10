from iiif_prezi3 import Manifest, CanvasRef, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
base_url = "https://iiif.io/api/cookbook/recipe/0024-book-4-toc"

image_base = "https://iiif.io/api/image/3.0/example/reference/d3bbf5397c6df6b894c5991195c912ab"

manifest = Manifest(
    id=f"{base_url}/manifest.json",
    label="Ethiopic Ms 10",
)

canvases = []
canvas_data = [
    ("p1", "f. 1r", "1-21198-zz001d8m41_774608_master", "p0001"),
    ("p2", "f. 1v", "2-21198-zz001d8m5j_774612_master", "p0002"),
    ("p3", "f. 2r", "3-21198-zz001d8tm5_775004_master", "p0003"),
    ("p4", "f. 2v", "4-21198-zz001d8tnp_775007_master", "p0004"),
    ("p5", "f. 3r", "5-21198-zz001d8v6f_775077_master", "p0005"),
    ("p6", "f. 3v", "6-21198-zz001d8v7z_775085_master", "p0006"),
]

for canvas_id, label, image_id, anno_num in canvas_data:
    canvas = manifest.make_canvas_from_iiif(
        url=f"{image_base}-{image_id}",
        id=f"{base_url}/canvas/{canvas_id}",
        label=label,
        anno_id=f"{base_url}/annotation/{anno_num}-image",
        anno_page_id=f"{base_url}/page/{canvas_id}/1",
    )
    canvases.append(canvas)

# Table of Contents (structures)
toc = manifest.make_range(
    id=f"{base_url}/range/r0",
    label="Table of Contents",
)

r1 = toc.make_range(
    id=f"{base_url}/range/r1",
    label={"gez": ["Tabiba Tabiban [\u1320\u1262\u1260 \u1320\u1262\u1263\u1295]"]},
)
r1.add_item(CanvasRef(id=f"{base_url}/canvas/p1", type="Canvas"))
r1.add_item(CanvasRef(id=f"{base_url}/canvas/p2", type="Canvas"))

r2 = toc.make_range(
    id=f"{base_url}/range/r2",
    label={"gez": ["Arede'et [\u12A0\u122D\u12F5\u12D5\u1275]"]},
)

r2_monday = r2.make_range(
    id=f"{base_url}/range/r2/1",
    label="Monday",
)
r2_monday.add_item(CanvasRef(id=f"{base_url}/canvas/p3", type="Canvas"))
r2_monday.add_item(CanvasRef(id=f"{base_url}/canvas/p4", type="Canvas"))

r2_tuesday = r2.make_range(
    id=f"{base_url}/range/r2/2",
    label="Tuesday",
)
r2_tuesday.add_item(CanvasRef(id=f"{base_url}/canvas/p5", type="Canvas"))
r2_tuesday.add_item(CanvasRef(id=f"{base_url}/canvas/p6", type="Canvas"))

print(manifest.json(indent=2))
