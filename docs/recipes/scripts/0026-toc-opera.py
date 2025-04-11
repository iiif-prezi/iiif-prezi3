from iiif_prezi3 import Manifest, ResourceItem, config, Annotation, AnnotationPage, CanvasRef

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "it"
base_url = "https://iiif.io/api/cookbook/recipe/0026-toc-opera"

manifest = Manifest(
    label = {
        "it": ["L'Elisir D'Amore"],
        "en": ["The Elixir of Love"]
    }
)
canvas = manifest.make_canvas(id=f"{base_url}/canvas/1")
anno_body = ResourceItem(
    id="https://fixtures.iiif.io/video/indiana/donizetti-elixir/vae0637_accessH264_low.mp4",
    type="Video",
    format="video/mp4"
)
anno_page = AnnotationPage(id=f"{base_url}/canvas/1/annotation_page/1")
anno = Annotation(
    id=f"{base_url}/canvas/1/annotation_page/1/annotation/1",
    motivation="painting",
    body=anno_body,
    target=canvas.id
)
hwd = { "width": 1920, "height": 1080, "duration": 7278.422 }
canvas.set_hwd(**hwd)
anno_body.set_hwd(**hwd)
anno_page.add_item(anno)
canvas.add_item(anno_page)
top_range = manifest.make_range(
    id=f"{base_url}/range/2",
    label="Atto Primo",
)
range_three = top_range.make_range(
    id=f"{base_url}/range/3",
    label="Preludio e Coro d'introduzione – Bel conforto al mietitore"
)
range_three.add_item(
    CanvasRef(
        id=f"{base_url}/canvas/1#t=0,302.05",
        type="Canvas"
    )
)

print(manifest.json(indent=2))