from iiif_prezi3 import Manifest, ResourceItem, AnnotationPage, Annotation, config, HomepageItem

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "none"
homepage = HomepageItem(
    id="https://www.getty.edu/art/collection/object/103RQQ",
    type="Text",
    label={"en": ["Home page at the Getty Museum Collection"]},
    format="text/html",
    language="en",
)
manifest = Manifest(
    id="https://iiif.io/api/cookbook/recipe/0047-homepage/manifest.json",
    label="Laocöon",
    homepage=homepage,
)
canvas = manifest.make_canvas(
    id="https://iiif.io/api/cookbook/recipe/0047-homepage/canvas/1",
    label="Front"
)
anno_body = ResourceItem(
    id="https://iiif.io/api/image/3.0/example/reference/28473c77da3deebe4375c3a50572d9d3-laocoon/full/!500,500/0/default.jpg",
    type="Image",
    format="image/jpeg"
)
anno_body.make_service(
    id="https://iiif.io/api/image/3.0/example/reference/28473c77da3deebe4375c3a50572d9d3-laocoon",
            type="ImageService3",
            profile="level1"
)
anno_page = AnnotationPage(
    id="https://iiif.io/api/cookbook/recipe/0047-homepage/canvas/1/page/1"
)
hw = {"height": 3000, "width": 2315}
anno_body.set_hwd(**hw)
canvas.set_hwd(**hw)
anno = Annotation(
    id="https://iiif.io/api/cookbook/recipe/0047-homepage/canvas/1/page/1/annotation/1",
    motivation="painting",
    body=anno_body,
    target=canvas.id
)
anno_page.add_item(anno)
canvas.add_item(anno_page)
print(manifest.json(indent=2))
