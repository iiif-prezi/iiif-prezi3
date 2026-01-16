from iiif_prezi3 import Manifest, AnnotationBody, AnnotationPage, Annotation, KeyValueString, config, Choice

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
base_url = "https://iiif.io/api/cookbook/recipe/0074-multiple-language-captions"

manifest = Manifest(
    id=f"{base_url}/manifest.json",
    label="For ladies. French models",
    rights="http://rightsstatements.org/vocab/InC/1.0/",
    requiredStatement=KeyValueString(label="Rights", value="All rights reserved Cinecittà Luce spa")
)
manifest.add_label(language="it", value="Per voi signore. Modelli francesi")

canvas = manifest.make_canvas(
    id=f"{base_url}/canvas"
)
video_resource = AnnotationBody(
    id="https://fixtures.iiif.io/video/europeana/Per_voi_signore_Modelli_francesi.mp4",
    type="Video",
    format="video/mp4"
)
video_hwd = {"height": 384, "width": 288, "duration": 65.0}
video_resource.set_hwd(**video_hwd)
canvas.set_hwd(**video_hwd)
painting_annotation = Annotation(
    id=f"{base_url}/canvas/page/annotation",
    motivation="painting",
    body=video_resource,
    target=canvas.id
)
annotation_page = AnnotationPage(
    id=f"{base_url}/canvas/page"
)
annotation_page.add_item(painting_annotation)
canvas.add_item(annotation_page)

italian_captions = AnnotationBody(
    id=f"{base_url}/Per_voi_signore_Modelli_francesi_it.vtt",
    type="Text",
    format="text/vtt",
    language="it",
)
italian_captions.add_label(language="it", value="Sottotitoli in formato WebVTT")
english_captions = AnnotationBody(
    id=f"{base_url}/Per_voi_signore_Modelli_francesi_en.vtt",
    type="Text",
    format="text/vtt",
    language="en"
)
english_captions.add_label(language="en", value="Captions in WebVTT format")
choice = Choice(
    items=[english_captions, italian_captions],
)

caption_annotation = canvas.make_annotation(
    id=f"{base_url}/manifest.json/subtitles_captions-files-vtt",
    motivation="supplementing",
    body=choice,
    target=canvas.id,
    anno_page_id=f"{base_url}/manifest.json/anno/page/1"
)
print(manifest.json(indent=2))
