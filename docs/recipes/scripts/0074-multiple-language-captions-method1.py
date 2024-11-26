from iiif_prezi3 import Manifest, ResourceItem, AnnotationPage, Annotation

manifest = Manifest(
    id="https://iiif.io/api/cookbook/recipe/0074-multiple-language-captions/manifest.json",
    label={"it": ["Per voi signore. Modelli francesi"]},
    rights="http://rightsstatements.org/vocab/InC/1.0/",
    requiredStatement={
        "label": {
            "en": [
                "Rights"
            ]
        },
        "value": {
            "en": [
                "All rights reserved Cinecittà Luce spa"
            ]
        }
    }
)
manifest.add_label(
    language="en",
    value="For ladies. French models"
)
canvas = manifest.make_canvas(id="https://iiif.io/api/cookbook/recipe/0074-multiple-language-captions/canvas")
painting_anno_body = ResourceItem(
    id="https://fixtures.iiif.io/video/europeana/Per_voi_signore_Modelli_francesi.mp4",
    type="Video",
    format="video/mp4"
)
painting_anno_page = AnnotationPage(
    id="https://iiif.io/api/cookbook/recipe/0074-multiple-language-captions/canvas/page"
)
painting_anno = Annotation(
    id="https://iiif.io/api/cookbook/recipe/0074-multiple-language-captions/canvas/page/annotation",
    motivation="painting",
    body=painting_anno_body,
    target=canvas.id
)
hwd = {"height": 384, "width": 288, "duration": 65.0}
italian_captions = {
    "id": "https://iiif.io/api/cookbook/recipe/0074-multiple-language-captions/Per_voi_signore_Modelli_francesi_it.vtt",
    "type": "Text",
    "format": "text/vtt",
    "label": {
        "it": [
            "Sottotitoli in formato WebVTT"
        ]
    },
    "language": "it"
}
english_captions = {
    "id": "https://iiif.io/api/cookbook/recipe/0074-multiple-language-captions/Per_voi_signore_Modelli_francesi_en.vtt",
    "type": "Text",
    "format": "text/vtt",
    "label": {
        "en": [
            "Captions in WebVTT format"
        ]
    },
    "language": "en"
}
painting_anno_body.set_hwd(**hwd)
canvas.set_hwd(**hwd)
painting_anno_page.add_item(painting_anno)
canvas.add_item(painting_anno_page)
captions = canvas.make_annotation(
    id="https://iiif.io/api/cookbook/recipe/0074-multiple-language-captions/manifest.json/subtitles_captions-files-vtt",
    motivation="supplementing",
    body={
        "type": "Choice",
        "items": [
            english_captions,
            italian_captions
        ]
    },
    target="https://iiif.io/api/cookbook/recipe/0074-multiple-language-captions/canvas",
    anno_page_id="https://iiif.io/api/cookbook/recipe/0074-multiple-language-captions/manifest.json/anno/page/1"
)
print(manifest.json(indent=2))
