from iiif_prezi3 import Manifest, ResourceItem, AnnotationPage, Annotation, config, Choice

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
base_url = "https://iiif.io/api/cookbook/recipe/0033-choice"

manifest = Manifest(
    id=f"{base_url}/manifest.json",
    label="John Dee performing an experiment before Queen Elizabeth I."
)
canvas = manifest.make_canvas(
    id=f"{base_url}/page/p1/1",
)

natural_light = ResourceItem(
    id="https://iiif.io/api/image/3.0/example/reference/421e65be2ce95439b3ad6ef1f2ab87a9-dee-natural/full/max/0/default.jpg",
    type="Image",
    format="image/jpeg",
    width=2000,
    height=1271,
)
natural_light.add_label(language="en", value="Natural Light")
natural_light.make_service(
    id="https://iiif.io/api/image/3.0/example/reference/421e65be2ce95439b3ad6ef1f2ab87a9-dee-natural",
    type="ImageService3",
    profile="level1"
)
x_ray = ResourceItem(
    id="https://iiif.io/api/image/3.0/example/reference/421e65be2ce95439b3ad6ef1f2ab87a9-dee-xray/full/max/0/default.jpg",
    type="Image",
    format="image/jpeg",
    width=2000,
    height=1271,
)
x_ray.add_label(language="en", value="X-Ray")
x_ray.make_service(
    id="https://iiif.io/api/image/3.0/example/reference/421e65be2ce95439b3ad6ef1f2ab87a9-dee-xray",
    type="ImageService3",
    profile="level1"
)
choice = Choice(
    items=[natural_light, x_ray],
)
canvas.add_annotation(
    anno_page_id=f"{base_url}/page/p1/1",
    annotation=Annotation(
        id=f"{base_url}/annotation/p0001-image",
        motivation="painting",
        body=choice,
        target=f"{base_url}/canvas/p1"
    ),
)

print(manifest.json(indent=2))
