from iiif_prezi3 import Manifest, ResourceItem, AnnotationPage, Annotation, config, AccompanyingCanvas

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
accompanying_canvas = AccompanyingCanvas(
    id="https://iiif.io/api/cookbook/recipe/0014-accompanyingcanvas/canvas/accompanying",
    label="First page of score for Gustav Mahler, Symphony No. 3",
    height=998,
    width=772,
)
manifest = Manifest(
    id="https://iiif.io/api/cookbook/recipe/0014-accompanyingcanvas/manifest.json",
    label="Partial audio recording of Gustav Mahler's _Symphony No. 3_",
)
ac_anno_body = ResourceItem(
    id="https://iiif.io/api/image/3.0/example/reference/4b45bba3ea612ee46f5371ce84dbcd89-mahler-0/full/,998/0/default.jpg",
    type="Image",
    format="image/jpeg",
    height=998,
    width=772,
)
ac_anno_body.make_service(
    id="https://iiif.io/api/image/3.0/example/reference/4b45bba3ea612ee46f5371ce84dbcd89-mahler-0",
    type="ImageService3",
    profile="level1"
)
ac_anno_page = AnnotationPage(
    id="https://iiif.io/api/cookbook/recipe/0014-accompanyingcanvas/canvas/accompanying/annotation/page"
)
ac_anno = Annotation(
    id="https://iiif.io/api/cookbook/recipe/0014-accompanyingcanvas/canvas/accompanying/annotation/image",
    motivation="painting",
    body=ac_anno_body,
    target="https://iiif.io/api/cookbook/recipe/0014-accompanyingcanvas/canvas/accompanying"
)
ac_anno_page.add_item(ac_anno)
accompanying_canvas.add_item(ac_anno_page)
canvas = manifest.make_canvas(
    id="https://iiif.io/api/cookbook/recipe/0014-accompanyingcanvas/canvas/p1",
    label="Gustav Mahler, Symphony No. 3, CD 1",
    height=998,
    width=772,
    duration=1985.024,
    accompanyingCanvas=accompanying_canvas
)
anno_body = ResourceItem(
    id="https://fixtures.iiif.io/audio/indiana/mahler-symphony-3/CD1/medium/128Kbps.mp4",
    type="Sound",
    format="video/mp4",
    duration=1985.024,
)
anno_page = AnnotationPage(
    id="https://iiif.io/api/cookbook/recipe/0014-accompanyingcanvas/canvas/page/p1"
)
anno = Annotation(
    id="https://iiif.io/api/cookbook/recipe/0014-accompanyingcanvas/canvas/page/annotation/segment1-audio",
    motivation="painting",
    body=anno_body,
    target=canvas.id
)
anno_page.add_item(anno)
canvas.add_item(anno_page)
print(manifest.json(indent=2))
