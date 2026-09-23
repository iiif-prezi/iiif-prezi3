from iiif_prezi3 import Manifest, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
base_url = "https://iiif.io/api/cookbook/recipe/0240-navPlace-on-canvases"

manifest = Manifest(
    id=f"{base_url}/manifest.json",
    label="Laocöon, geolocated sculpture and painting.",
)
manifest.add_context("http://iiif.io/api/extension/navplace/context.json")

canvas1 = manifest.make_canvas_from_iiif(
    url="https://iiif.io/api/image/3.0/example/reference/28473c77da3deebe4375c3a50572d9d3-laocoon",
    id=f"{base_url}/canvas/1",
    label="Front of Bronze",
    anno_id=f"{base_url}/anno/1",
    anno_page_id=f"{base_url}/anno-page/1",
)
canvas1.add_navplace_feature(
    id=f"{base_url}/feature/1",
    label={
        "en": ["Current Location of the Laocoön Bronze"],
        "it": ["Ubicazione attuale del Bronzo Laocoonte e i suoi figli"],
    },
    geometry={
        "type": "Point",
        "coordinates": [-118.4745559, 34.0776376],
    },
    feature_collection_id=f"{base_url}/feature-collection/1",
)

canvas2 = manifest.make_canvas_from_iiif(
    url="https://iiif.io/api/image/3.0/example/reference/58763298b61c2a99f78ff94d8364c639-laocoon_1946_18_1",
    id=f"{base_url}/canvas/2",
    label="Painting",
    anno_id=f"{base_url}/anno/2",
    anno_page_id=f"{base_url}/anno-page/2",
)
canvas2.add_navplace_feature(
    id=f"{base_url}/feature/2",
    label={
        "en": ["Current Location of Painting"],
    },
    geometry={
        "type": "Point",
        "coordinates": [-77.0199025, 38.8920717],
    },
    feature_collection_id=f"{base_url}/feature-collection/2",
)

print(manifest.json(indent=2))
