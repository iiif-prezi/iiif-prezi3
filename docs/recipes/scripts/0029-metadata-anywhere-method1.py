from iiif_prezi3 import Manifest, ResourceItem, AnnotationPage, Annotation, config, KeyValueString

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
base_url = "https://iiif.io/api/cookbook/recipe/0029-metadata-anywhere"

manifest = Manifest(
    id=f"{base_url}/manifest.json",
    label = "John Dee performing an experiment before Queen Elizabeth I.",
    metadata=[
        KeyValueString(
            label="Creator",
            value="Glindoni, Henry Gillard, 1852-1913"
        ),
        KeyValueString(
            label="Date",
            value="1800-1899"
        ),
        KeyValueString(
            label="Physical Description",
            value="1 painting : oil on canvas ; canvas 152 x 244.4 cm"
        ),
        KeyValueString(
            label="Reference",
            value="Wellcome Library no. 47369i"
        )
    ],
    requiredStatement=KeyValueString(
        label="Attribution",
        value="Wellcome Collection. Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)"
    )
)
hw = {"height": 1271, "width": 2000}
canvas = manifest.make_canvas(
    id=f"{base_url}/canvas/p1",
    label="Painting under natural light",
    metadata=[
        KeyValueString(
            label="Description",
            value="The scene is the house at Mortlake of Dr John Dee (1527-1608). At the court of Queen Elizabeth I, Dee was revered for the range of his scientific knowledge, which embraced the fields of mathematics, navigation, geography, alchemy/chemistry, medicine and optics. In the painting he is showing the effect of combining two elements, either to cause combustion or to extinguish it. Behind him is his assistant Edward Kelly, wearing a long skullcap to conceal the fact that his ears had been cropped as a punishment for forgery."
        )
    ]
)
canvas.set_hwd(**hw)
anno_body = ResourceItem(
    id="https://iiif.io/api/image/3.0/example/reference/421e65be2ce95439b3ad6ef1f2ab87a9-dee-natural/full/max/0/default.jpg",
    type="Image",
    format="image/jpeg",
)
anno_body.set_hwd(**hw)
anno_body.make_service(
    id="https://iiif.io/api/image/3.0/example/reference/421e65be2ce95439b3ad6ef1f2ab87a9-dee-natural",
    profile="level1",
    type="ImageService3",
)
anno_page = AnnotationPage(
    id=f"{base_url}/page/p1/1"
)
anno = Annotation(
    id=f"{base_url}/annotation/p0001-image",
    motivation="painting",
    body=anno_body,
    target=f"{base_url}/canvas/p1"
)
anno_page.add_item(anno)
canvas.add_item(anno_page)
canvas_2 = manifest.make_canvas(
    id=f"{base_url}/canvas/p2",
    label="X-ray view of painting",
    metadata=[
        KeyValueString(
            label="Description",
            value="The painting originally showed Dee standing in a circle of skulls on the floor, stretching from the floor area in front of the Queen (on the left) to the floor near Edward Kelly (on the right). The skulls were at an early stage painted over, but have since become visible. Another pentimento is visible in the tapestry on the right: shelves containing monstrous animals are visible behind it. The pentimenti were clarified when the painting was X-rayed in 2015."
        )
    ]
)
canvas_2.set_hwd(**hw)
anno_body_2 = ResourceItem(
    id="https://iiif.io/api/image/3.0/example/reference/421e65be2ce95439b3ad6ef1f2ab87a9-dee-xray/full/max/0/default.jpg",
    type="Image",
    format="image/jpeg",
)
anno_body_2.set_hwd(**hw)
anno_body_2.make_service(
    id="https://iiif.io/api/image/3.0/example/reference/421e65be2ce95439b3ad6ef1f2ab87a9-dee-xray",
    profile="level1",
    type="ImageService3",
)
anno_page_2 = AnnotationPage(
    id=f"{base_url}/page/p2/1"
)
anno2 = Annotation(
    id=f"{base_url}/annotation/p0002-image",
    motivation="painting",
    body=anno_body_2,
    target=f"{base_url}/canvas/p2"
)
anno_page_2.add_item(anno2)
canvas_2.add_item(anno_page_2)

print(manifest.json(indent=2))
