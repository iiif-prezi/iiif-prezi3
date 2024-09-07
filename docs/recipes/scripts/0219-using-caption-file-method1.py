from iiif_prezi3 import Manifest, ResourceItem, AnnotationPage, Annotation, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
manifest = Manifest(
    id="https://iiif.io/api/cookbook/recipe/0219-using-caption-file/manifest.json",
    label="Lunchroom Manners"
)
canvas = manifest.make_canvas(id="https://iiif.io/api/cookbook/recipe/0219-using-caption-file/canvas")
painting_anno_body = ResourceItem(
    id="https://fixtures.iiif.io/video/indiana/lunchroom_manners/high/lunchroom_manners_1024kb.mp4",
    type="Video",
    format="video/mp4"
)
painting_anno_page = AnnotationPage(
    id="https://iiif.io/api/cookbook/recipe/0219-using-caption-file/canvas/page"
)
painting_anno = Annotation(
    id="https://iiif.io/api/cookbook/recipe/0219-using-caption-file/canvas/page/annotation1",
    motivation="painting",
    body=painting_anno_body,
    target=canvas.id
)
hwd = {"height": 360, "width": 480, "duration": 572.034}
painting_anno_body.set_hwd(**hwd)
canvas.set_hwd(**hwd)
painting_anno_page.add_item(painting_anno)
canvas.add_item(painting_anno_page)
captions = canvas.make_annotation(
    id="https://iiif.io/api/cookbook/recipe/0219-using-caption-file/canvas/page2/a1",
    motivation="supplementing",
    body={
        "id": "https://fixtures.iiif.io/video/indiana/lunchroom_manners/lunchroom_manners.vtt",
        "type": "Text",
        "language": "en",
        "format": "text/vtt",
        "label": {
            "en": [
                "Captions in WebVTT format"
            ]
        }
    },
    target="https://iiif.io/api/cookbook/recipe/0219-using-caption-file/canvas",
    anno_page_id="https://iiif.io/api/cookbook/recipe/0219-using-caption-file/canvas/page2"
)
print(manifest.json(indent=2))
