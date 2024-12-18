from iiif_prezi3 import Manifest, ResourceItem, AnnotationPage, Annotation, config, PlaceholderCanvas

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
base_url = "https://iiif.io/api/cookbook/recipe/0013-placeholderCanvas"

manifest = Manifest(
    id=f"{base_url}/manifest.json",
    label="Video recording of Donizetti's _The Elixer of Love_",
)
placeholder_canvas = PlaceholderCanvas(
    id=f"{base_url}/canvas/donizetti/placeholder",
    width=640,
    height=360,
)
pc_anno_page = AnnotationPage(
    id=f"{base_url}/canvas/donizetti/placeholder/1"
)
pc_anno_body = ResourceItem(
    id="https://fixtures.iiif.io/video/indiana/donizetti-elixir/act1-thumbnail.png",
    type="Image",
    format="image/png",
    width=640,
    height=360,
)
pc_anno = Annotation(
    id=f"{base_url}/canvas/donizetti/placeholder/1-image",
    motivation="painting",
    body=pc_anno_body,
    target=f"{base_url}/canvas/donizetti/placeholder"
)
pc_anno_page.add_item(pc_anno)
placeholder_canvas.add_item(pc_anno_page)

canvas = manifest.make_canvas(
    id=f"{base_url}/canvas/donizetti",
    duration=7278.466,
    height=360,
    width=640,
    placeholderCanvas=placeholder_canvas,
)

anno_body = ResourceItem(
    id="https://fixtures.iiif.io/video/indiana/donizetti-elixir/vae0637_accessH264_low.mp4",
    type="Video",
    duration=7278.466,
    width=640,
    height=360,
    format="video/mp4"
)
anno = Annotation(
    id=f"{base_url}/donizetti/1-video",
    motivation="painting",
    body=anno_body,
    target=canvas.id
)
anno_page = AnnotationPage(
    id=f"{base_url}/donizetti/1",
)
anno_page.add_item(anno)
canvas.add_item(anno_page)

print(manifest.json(indent=2))
