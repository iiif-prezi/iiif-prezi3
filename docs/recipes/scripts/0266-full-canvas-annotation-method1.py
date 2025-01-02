from iiif_prezi3 import Manifest, ResourceItem, AnnotationPage, Annotation, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
base_url = "https://iiif.io/api/cookbook/recipe/0266-full-canvas-annotation"

manifest = Manifest(
    id=f"{base_url}/manifest.json",
    label="Picture of Göttingen taken during the 2019 IIIF Conference",
)

anno_page = AnnotationPage(
    id=f"{base_url}/canvas-1/annopage-1"
)
painting_body = ResourceItem(
    id="https://iiif.io/api/image/3.0/example/reference/918ecd18c2592080851777620de9bcb5-gottingen/full/max/0/default.jpg",
    type="Image",
    format="image/jpeg",
)
painting_body.make_service(
    id="https://iiif.io/api/image/3.0/example/reference/918ecd18c2592080851777620de9bcb5-gottingen",
    type="ImageService3",
    profile="level1"
)
painting_anno = Annotation(
    id=f"{base_url}/canvas-1/annopage-1/anno-1",
    motivation="painting",
    body=painting_body,
    target=f"{base_url}/canvas-1"
)
anno_page.add_item(painting_anno)
hw = {"height": 3024, "width": 4032}
canvas = manifest.make_canvas(
    id=f"{base_url}/canvas-1",
)
painting_body.set_hwd(**hw)
canvas.set_hwd(**hw)
canvas.add_item(anno_page)
anno_body = ResourceItem(
    type="TextualBody",
    language="de",
    format="text/plain",
    value="Göttinger Marktplatz mit Gänseliesel Brunnen"
)
anno = canvas.make_annotation(
    id=f"{base_url}/canvas-1/annopage-2/anno-1",
    motivation="commenting",
    body=anno_body,
    target=canvas.id
)

print(manifest.json(indent=2))