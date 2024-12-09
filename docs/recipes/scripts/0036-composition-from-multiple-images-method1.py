from iiif_prezi3 import Manifest, ResourceItem, AnnotationPage, Annotation, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
base_url = "https://iiif.io/api/cookbook/recipe/0036-composition-from-multiple-images"

manifest = Manifest(
    id=f"{base_url}/manifest.json",
    label="Folio from Grandes Chroniques de France, ca. 1460"
)
canvas = manifest.make_canvas(
    id=f"{base_url}/canvas/p1",
    height=5412,
    width=7216
)
canvas.add_label(language="none", value="f. 033v-034r [Chilpéric Ier tue Galswinthe, se remarie et est assassiné]")

anno_body_a = ResourceItem(
    id="https://iiif.io/api/image/3.0/example/reference/899da506920824588764bc12b10fc800-bnf_chateauroux/full/max/0/default.jpg",
    type="Image",
    format="image/jpeg",
    height=5412,
    width=7216
)
anno_body_a.make_service(
    id="https://iiif.io/api/image/3.0/example/reference/899da506920824588764bc12b10fc800-bnf_chateauroux",
    type="ImageService3",
    profile="level1"
)
anno_page = AnnotationPage(
    id=f"{base_url}/page/p1/1"
)
annotation_a = Annotation(
    id=f"{base_url}/annotation/p0001-image",
    motivation="painting",
    body=anno_body_a,
    target=canvas.id
)

anno_body_b = ResourceItem(
    id="https://iiif.io/api/image/3.0/example/reference/899da506920824588764bc12b10fc800-bnf_chateauroux_miniature/full/max/0/default.jpg",
    type="Image",
    format="image/jpeg",
    width=2138,
    height=2414
)
anno_body_b.add_label(language="fr", value="Miniature [Chilpéric Ier tue Galswinthe, se remarie et est assassiné]")
anno_body_b.make_service(
    id="https://iiif.io/api/image/3.0/example/reference/899da506920824588764bc12b10fc800-bnf_chateauroux_miniature",
    type="ImageService3",
    profile="level1"
)
annotation_b = Annotation(
    id=f"{base_url}/annotation/p0002-image",
    motivation="painting",
    body=anno_body_b,
    target=f"{canvas.id}#xywh=3949,994,1091,1232"
)

anno_page.add_item(annotation_a)
anno_page.add_item(annotation_b)
canvas.add_item(anno_page)

print(manifest.json(indent=2))