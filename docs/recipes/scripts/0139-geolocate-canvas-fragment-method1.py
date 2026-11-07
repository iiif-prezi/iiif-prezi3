from iiif_prezi3 import Manifest, config
from iiif_prezi3.skeleton import Annotation, AnnotationPage

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
base_url = "https://iiif.io/api/cookbook/recipe/0139-geolocate-canvas-fragment"

manifest = Manifest(
    id=f"{base_url}/manifest.json",
    label="Recipe Manifest for #139",
    summary="A IIIF Presentation API 3.0 Manifest containing a GeoJSON-LD Web Annotation which targets a Canvas fragment.",
)
manifest.add_context("http://geojson.org/geojson-ld/geojson-context.jsonld")

canvas = manifest.make_canvas_from_iiif(
    url="https://iiif.io/api/image/3.0/example/reference/43153e2ec7531f14dd1c9b2fc401678a-88695674",
    id=f"{base_url}/canvas.json",
    label="Chesapeake and Ohio Canal Pamphlet",
    anno_id=f"{base_url}/content.json",
    anno_page_id=f"{base_url}/contentPage.json",
)

# Use model_construct to bypass Annotation body validation, which allows
# a GeoJSON Feature (with properties and geometry) to be used as the body.
geo_anno = Annotation.model_construct(
    id=f"{base_url}/geoAnno.json",
    type="Annotation",
    motivation="tagging",
    body={
        "id": f"{base_url}/geo.json",
        "type": "Feature",
        "properties": {
            "label": {
                "en": ["Targeted Map from Chesapeake and Ohio Canal Pamphlet"]
            }
        },
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [-77.019853, 38.913101],
                    [-77.110013, 38.843254],
                    [-77.284698, 38.997574],
                    [-77.188911, 39.062648],
                ]
            ],
        },
    },
    target=f"{canvas.id}#xywh=920,3600,1510,3000",
)

anno_page = AnnotationPage(
    id=f"{base_url}/supplementingPage.json",
    items=[geo_anno],
)
canvas.annotations = [anno_page]

print(manifest.json(indent=2))
