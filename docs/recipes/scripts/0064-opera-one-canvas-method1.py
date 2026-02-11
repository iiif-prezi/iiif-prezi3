from iiif_prezi3 import (Manifest, Canvas, AnnotationBody, AnnotationPage,
                        Annotation, CanvasRef, KeyValueString, config)

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
base_url = "https://iiif.io/api/cookbook/recipe/0064-opera-one-canvas"

manifest = Manifest(
    id=f"{base_url}/manifest.json",
    label="The Elixir of Love",
    metadata=[
        KeyValueString(
            label={"en": ["Date Issued"]},
            value={"en": ["2019"]},
        ),
        KeyValueString(
            label={"en": ["Publisher"]},
            value={"en": ["Indiana University Jacobs School of Music"]},
        ),
    ],
)
manifest.add_label("L'Elisir D'Amore", "it")

canvas = Canvas(
    id=f"{base_url}/canvas/1",
    width=1920,
    height=1080,
    duration=7278.422,
)

anno_page = AnnotationPage(id=f"{base_url}/canvas/1/annotation_page/1")

act1_body = AnnotationBody(
    id="https://fixtures.iiif.io/video/indiana/donizetti-elixir/vae0637_accessH264_low_act_1.mp4",
    type="Video",
    format="video/mp4",
    height=1080,
    width=1920,
)
act1_body.duration = 3971.24
anno_page.add_item(
    Annotation(
        id=f"{base_url}/canvas/1/annotation_page/1/annotation/1",
        motivation="painting",
        target=f"{base_url}/canvas/1#t=0,3971.24",
        body=act1_body,
    )
)

act2_body = AnnotationBody(
    id="https://fixtures.iiif.io/video/indiana/donizetti-elixir/vae0637_accessH264_low_act_2.mp4",
    type="Video",
    format="video/mp4",
    height=1080,
    width=1920,
)
act2_body.duration = 3307.22
anno_page.add_item(
    Annotation(
        id=f"{base_url}/canvas/1/annotation_page/1/annotation/2",
        motivation="painting",
        target=f"{base_url}/canvas/1#t=3971.24",
        body=act2_body,
    )
)

canvas.add_item(anno_page)
canvas.add_thumbnail(
    "https://fixtures.iiif.io/video/indiana/donizetti-elixir/act1-thumbnail.png",
)
manifest.add_item(canvas)

# Structures
top_range = manifest.make_range(
    id=f"{base_url}/range/1",
)
top_range.add_label("Gaetano Donizetti, L'Elisir D'Amore", "it")

range_atto1 = top_range.make_range(
    id=f"{base_url}/range/2",
)
range_atto1.add_label("Atto Primo", "it")

range_preludio = range_atto1.make_range(
    id=f"{base_url}/range/3",
)
range_preludio.add_label("Preludio e Coro d'introduzione \u2013 Bel conforto al mietitore", "it")
range_preludio.add_item(
    CanvasRef(id=f"{base_url}/canvas/1#t=0,302.05", type="Canvas")
)

range_remainder = range_atto1.make_range(
    id=f"{base_url}/range/4",
    label="Remainder of Atto Primo",
)
range_remainder.add_item(
    CanvasRef(id=f"{base_url}/canvas/1#t=302.05,3971.24", type="Canvas")
)

range_atto2 = top_range.make_range(
    id=f"{base_url}/range/5",
)
range_atto2.add_label("Atto Secondo", "it")
range_atto2.add_item(
    CanvasRef(id=f"{base_url}/canvas/1#t=3971.24,7278.422", type="Canvas")
)

print(manifest.json(indent=2))
