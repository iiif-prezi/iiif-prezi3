from iiif_prezi3 import Manifest, LinkedResource, AnnotationBody, AnnotationPage, Annotation, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
base_url = "https://iiif.io/api/cookbook/recipe/0017-transcription-av"

manifest = Manifest(id=f"{base_url}/manifest.json",
                    label="Volleyball for Boys")

canvas = manifest.make_canvas(id=f"{base_url}/canvas")
anno_body = AnnotationBody(id="https://fixtures.iiif.io/video/indiana/volleyball/high/volleyball-for-boys.mp4",
                         type="Video",
                         format="video/mp4")
anno_page = AnnotationPage(id=f"{base_url}/canvas/page")
anno = Annotation(id=f"{base_url}/canvas/page/annotation",
                  motivation="painting",
                  body=anno_body,
                  target=canvas.id)

hwd = {"height": 1080, "width": 1920, "duration": 662.037}
anno_body.set_hwd(**hwd)
canvas.set_hwd(**hwd)

anno_page.add_item(anno)
canvas.add_item(anno_page)

rendering = LinkedResource(id="https://fixtures.iiif.io/video/indiana/volleyball/volleyball.txt",
                         type="Text",
                         label="Transcript",
                         format="text/plain")

canvas.rendering = [rendering]

print(manifest.json(indent=2))
