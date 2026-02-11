from iiif_prezi3 import (Manifest, AnnotationBody, AnnotationPage, Annotation,
                        SpecificResource, CssStylesheet, config)

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "ca"
base_url = "https://iiif.io/api/cookbook/recipe/0040-image-rotation-service"

manifest = Manifest(
    id=f"{base_url}/manifest-css.json",
    label="[Conoximent de las orines] Ihesus, Ihesus. En nom de Deu et dela beneyeta sa mare e de tots los angels i archangels e de tots los sants e santes de paradis yo micer Johannes comense aquest libre de reseptes en l’ayn Mi 466."
)

image_source = AnnotationBody(
    id="https://iiif.io/api/image/3.0/example/reference/85a96c630f077e6ac6cb984f1b752bbf-0-21198-zz00022840-1-page1/full/max/0/default.jpg",
    type="Image",
    format="image/jpeg",
    width=1523,
    height=2105,
)
image_source.make_service(
    id="https://iiif.io/api/image/3.0/example/reference/85a96c630f077e6ac6cb984f1b752bbf-0-21198-zz00022840-1-page1",
    type="ImageService3",
    profile="level1",
)

painting_body = SpecificResource(
    id=f"{base_url}/body/sr1",
    styleClass="rotated",
    source=image_source,
)

canvas = manifest.make_canvas(id=f"{base_url}/canvas/p1")
canvas.set_hwd(width=2105, height=1523)
canvas.add_label("inside cover; 1r", "en")

anno_page = AnnotationPage(id=f"{base_url}/p1/1")
anno_page.add_item(
    Annotation(
        id=f"{base_url}/annotation/v0001-image",
        motivation="painting",
        stylesheet=CssStylesheet(
            value=".rotated { transform-origin: 761px 1344px; transform: rotate(90deg) translateY(-582px); }",
        ),
        body=painting_body,
        target=canvas.id,
    )
)
canvas.add_item(anno_page)

print(manifest.json(indent=2))
