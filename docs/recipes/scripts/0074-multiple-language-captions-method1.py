from iiif_prezi3 import Manifest, ResourceItem, AnnotationPage, Annotation, KeyValueString, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
base_url = "https://iiif.io/api/cookbook/recipe/0074-multiple-language-captions"

def create_caption(id, format, label, language):
    return ResourceItem(
        id=id,
        type="Text",
        format=format,
        label=label,
        language=language
    )

manifest = Manifest(
    id=f"{base_url}/manifest.json",
    label={"it": ["Per voi signore. Modelli francesi"]},
    rights="http://rightsstatements.org/vocab/InC/1.0/",
    requiredStatement=KeyValueString(label="Rights", value="All rights reserved Cinecittà Luce spa")
)
manifest.add_label(language="en", value="For ladies. French models")

canvas = manifest.make_canvas(
    id=f"{base_url}/canvas"
)

video_resource = ResourceItem(
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

# Create caption choices
italian_captions = create_caption(
    id=f"{base_url}/Per_voi_signore_Modelli_francesi_it.vtt",
    format="text/vtt",
    label={"it": ["Sottotitoli in formato WebVTT"]},
    language="it"
)
english_captions = create_caption(
    id=f"{base_url}/Per_voi_signore_Modelli_francesi_en.vtt",
    format="text/vtt",
    label={"en": ["Captions in WebVTT format"]},
    language="en"
)

anno_body = ResourceItem(
    id="https://fixtures.iiif.io/video/indiana/lunchroom_manners/high/lunchroom_manners_1024kb.mp4",
    type="Choice",
    format="video/mp4"
)

# Add captions as a Choice annotation
caption_annotation = canvas.make_annotation(
    id=f"{base_url}/manifest.json/subtitles_captions-files-vtt",
    motivation="supplementing",
    body={
        "type": "Choice",
        "items": [english_captions, italian_captions]
    },
    target=canvas.id,
    anno_page_id=f"{base_url}/manifest.json/anno/page/1"
)

print(manifest.json(indent=2))
