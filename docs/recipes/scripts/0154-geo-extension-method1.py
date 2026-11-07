from iiif_prezi3 import Manifest, NavPlace

base_url = "https://iiif.io/api/cookbook/recipe/0154-geo-extension"

manifest = Manifest(
    id=f"{base_url}/manifest.json",
    label={"it": ["Bronzo Laocoonte e i suoi figli"]},
    navPlace=NavPlace(
        id=f"{base_url}/feature-collection/1",
        features=[{
            "id": f"{base_url}/feature/1",
            "type": "Feature",
            "properties": {
                "label": {
                    "en": ["The Laocoön Bronze"],
                    "it": ["Bronzo Laocoonte e i suoi figli"],
                }
            },
            "geometry": {
                "type": "Point",
                "coordinates": [-118.4745559, 34.0776376],
            },
        }],
    ),
)

manifest.add_context("http://iiif.io/api/extension/navplace/context.json")

canvas1 = manifest.make_canvas_from_iiif(
    url="https://iiif.io/api/image/3.0/example/reference/28473c77da3deebe4375c3a50572d9d3-laocoon",
    id=f"{base_url}/canvas/1",
    label={"en": ["Front of Bronze"]},
    anno_id=f"{base_url}/anno/1",
    anno_page_id=f"{base_url}/anno-page/1",
)

print(manifest.json(indent=2))
