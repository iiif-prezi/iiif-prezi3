from iiif_prezi3 import Manifest, AnnotationBody, config, Annotation, AnnotationPage, CanvasRef

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "it"
base_url = "https://iiif.io/api/cookbook/recipe/0026-toc-opera"

manifest = Manifest(
    id=f"{base_url}/manifest.json",
    label="L'Elisir D'Amore"
)
manifest.add_label("The Elixir of Love", "en")
canvas = manifest.make_canvas(id=f"{base_url}/canvas/1")
anno_body = AnnotationBody(
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
hwd = {"width": 1920, "height": 1080, "duration": 7278.422}
canvas.set_hwd(**hwd)
anno_body.set_hwd(**hwd)
anno_page.add_item(anno)
canvas.add_item(anno_page)

# Create Ranges with Make Range and Add Item
top_range = manifest.make_range(
    id=f"{base_url}/range/1",
    label="Gaetano Donizetti, L'Elisir D'Amore",
)
range_two = top_range.make_range(
    id=f"{base_url}/range/2",
    label="Atto Primo",
)
range_three = range_two.make_range(
    id=f"{base_url}/range/3",
    label="Preludio e Coro d'introduzione – Bel conforto al mietitore"
)
range_three.add_item(
    CanvasRef(
        id=f"{base_url}/canvas/1#t=0,302.05",
        type="Canvas"
    )
)
range_four = range_two.make_range(
    id=f"{base_url}/range/4"
)
range_four.add_label(
    "Remainder of Atto Primo",
    "en"
)
range_four.add_item(
    CanvasRef(
        id=f"{base_url}/canvas/1#t=302.05,3971.24",
        type="Canvas"
    )
)
range_five = top_range.make_range(
    id=f"{base_url}/range/5",
    label="Atto Secondo",
)
range_five.add_item(
    CanvasRef(
        id=f"{base_url}/canvas/1#t=3971.24",
        type="Canvas"
    )
)

print(manifest.json(indent=2))
