from iiif_prezi3 import Manifest, AnnotationBody, AnnotationPage, Annotation, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
base_url = "https://iiif.io/api/cookbook/recipe/0219-using-caption-file"

manifest = Manifest(
    id=f"{base_url}/manifest.json",
    label="Lunchroom Manners"
)
canvas = manifest.make_canvas(id=f"{base_url}/canvas")
painting_anno_body = AnnotationBody(
    id="https://fixtures.iiif.io/video/indiana/lunchroom_manners/high/lunchroom_manners_1024kb.mp4",
    type="Video",
    format="video/mp4"
)
painting_anno_page = AnnotationPage(
    id=f"{base_url}/canvas/page"
)
painting_anno = Annotation(
    id=f"{base_url}/canvas/page/annotation1",
    motivation="painting",
    body=painting_anno_body,
    target=canvas.id
)
hwd = {"height": 360, "width": 480, "duration": 572.034}
painting_anno_body.set_hwd(**hwd)
canvas.set_hwd(**hwd)
painting_anno_page.add_item(painting_anno)
canvas.add_item(painting_anno_page)
caption_body = AnnotationBody(
    id="https://fixtures.iiif.io/video/indiana/lunchroom_manners/lunchroom_manners.vtt",
    type="Text",
    language="en",
    format="text/vtt"
)
caption_body.add_label(language="en", value="Captions in WebVTT format")
captions = canvas.make_annotation(
    id=f"{base_url}/canvas/page2/a1",
    motivation="supplementing",
    body=caption_body,
    target=f"{base_url}/canvas",
    anno_page_id=f"{base_url}/canvas/page2"
)
print(manifest.json(indent=2))
