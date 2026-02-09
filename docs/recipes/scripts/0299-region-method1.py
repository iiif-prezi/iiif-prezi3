from iiif_prezi3 import Manifest, AnnotationBody, AnnotationPage, Annotation, SpecificResource, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
base_url = "https://iiif.io/api/cookbook/recipe/0299-region"

manifest = Manifest(
    id=f"{base_url}/manifest.json",
    label="Berliner Tageblatt article, 'Ein neuer Sicherungsplan?'",
)

image_source = AnnotationBody(
    id="https://iiif.io/api/image/3.0/example/reference/4ce82cef49fb16798f4c2440307c3d6f-newspaper-p2/full/max/0/default.jpg",
    type="Image",
    format="image/jpeg",
    height=4999,
    width=3536,
)
image_source.make_service(
    id="https://iiif.io/api/image/3.0/example/reference/4ce82cef49fb16798f4c2440307c3d6f-newspaper-p2",
    type="ImageService3",
    profile="level1",
)

painting_body = SpecificResource(
    id=f"{base_url}/body/b1",
    source=image_source,
    selector={"type": "ImageApiSelector", "region": "1768,2423,1768,2080"},
)

anno_page = AnnotationPage(id=f"{base_url}/page/p1/1")
anno_page.add_item(
    Annotation(
        id=f"{base_url}/annotation/p0001-image",
        motivation="painting",
        body=painting_body,
        target=f"{base_url}/canvas/p1",
    )
)

canvas = manifest.make_canvas(id=f"{base_url}/canvas/p1")
canvas.set_hwd(height=2080, width=1768)
canvas.add_item(anno_page)

print(manifest.json(indent=2))
