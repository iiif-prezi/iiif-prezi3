from iiif_prezi3 import Manifest, AnnotationPage, Annotation, AnnotationBody, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
base_url = "https://iiif.io/api/cookbook/recipe/0003-mvm-video"

manifest = Manifest(id=f"{base_url}/manifest.json", label="Video Example 3")
canvas = manifest.make_canvas(id=f"{base_url}/canvas")
anno_body = AnnotationBody(id="https://fixtures.iiif.io/video/indiana/lunchroom_manners/high/lunchroom_manners_1024kb.mp4",
                         type="Video",
                         format="video/mp4")
anno_page = AnnotationPage(id=f"{base_url}/canvas/page")
anno = Annotation(id=f"{base_url}/canvas/page/annotation",
                  motivation="painting",
                  body=anno_body,
                  target=canvas.id)

hwd = {"height": 360, "width": 480, "duration": 572.034}
anno_body.set_hwd(**hwd)
canvas.set_hwd(**hwd)

anno_page.add_item(anno)
canvas.add_item(anno_page)

print(manifest.json(indent=2))
