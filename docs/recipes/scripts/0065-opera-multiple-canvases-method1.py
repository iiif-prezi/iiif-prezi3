from iiif_prezi3 import (Manifest, Canvas, AnnotationBody, AnnotationPage,
                        Annotation, CanvasRef, KeyValueString, config)

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
base_url = "https://iiif.io/api/cookbook/recipe/0065-opera-multiple-canvases"

manifest = Manifest(
    id=f"{base_url}/manifest.json",
    label="The Elixir of Love",
    metadata=[
        KeyValueString(
            label="Date Issued",
            value="2019",
        ),
        KeyValueString(
            label="Publisher",
            value="Indiana University Jacobs School of Music",
        ),
    ],
)
manifest.add_label("L'Elisir D'Amore", "it")

# Canvas data: (canvas_id, label, video_file, duration, thumbnail)
canvas_data = [
    ("1", "Atto Primo", "vae0637_accessH264_low_act_1.mp4", 3971.24, "act1-thumbnail.png"),
    ("2", "Atto Secondo", "vae0637_accessH264_low_act_2.mp4", 3307.22, "act2-thumbnail.png"),
]

video_base = "https://fixtures.iiif.io/video/indiana/donizetti-elixir"

for canvas_id, label, video_file, duration, thumb_file in canvas_data:
    canvas = Canvas(
        id=f"{base_url}/canvas/{canvas_id}",
        width=1920,
        height=1080,
        duration=duration,
        label=label,
    )

    body = AnnotationBody(
        id=f"{video_base}/{video_file}",
        type="Video",
        format="video/mp4",
        height=1080,
        width=1920,
    )
    body.duration = duration

    anno_page = AnnotationPage(id=f"{base_url}/canvas/{canvas_id}/annotation_page/1")
    anno_page.add_item(
        Annotation(
            id=f"{base_url}/canvas/{canvas_id}/annotation_page/1/annotation/1",
            motivation="painting",
            target=f"{base_url}/canvas/{canvas_id}",
            body=body,
        )
    )
    canvas.add_item(anno_page)
    canvas.add_thumbnail(f"{video_base}/{thumb_file}")
    manifest.add_item(canvas)

top_range = manifest.make_range(
    id=f"{base_url}/range/1",
)
top_range.add_label("Gaetano Donizetti, L'Elisir D'Amore", "it")

range_atto1 = top_range.make_range(
    id=f"{base_url}/range/2",
    label="Atto Primo",
)

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
    label="Atto Secondo",
)
range_atto2.add_item(
    CanvasRef(id=f"{base_url}/canvas/2#t=0,3307.22", type="Canvas")
)

print(manifest.json(indent=2))
