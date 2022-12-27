from iiif_prezi3 import Manifest, ExternalItem, ResourceItem, AnnotationPage, Annotation, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
manifest = Manifest(id="https://iiif.io/api/cookbook/recipe/0017-transcription-av/manifest.json",
                    label="Volleyball for Boys")

canvas = manifest.make_canvas(id="https://iiif.io/api/cookbook/recipe/0017-transcription-av/canvas")
anno_body = ResourceItem(id="https://fixtures.iiif.io/video/indiana/volleyball/high/volleyball-for-boys.mp4",
                         type="Video",
                         format="video/mp4")
anno_page = AnnotationPage(id="https://iiif.io/api/cookbook/recipe/0017-transcription-av/canvas/page")
anno = Annotation(id="https://iiif.io/api/cookbook/recipe/0017-transcription-av/canvas/page/annotation",
                  motivation="painting",
                  body=anno_body,
                  target=canvas.id)

hwd = {"height": 1080, "width": 1920, "duration": 662.037}
anno_body.set_hwd(**hwd)
canvas.set_hwd(**hwd)

anno_page.add_item(anno)
canvas.add_item(anno_page)

rendering = ExternalItem(id="https://fixtures.iiif.io/video/indiana/volleyball/volleyball.txt",
                         type="Text",
                         label="Transcript",
                         format="text/txt")

canvas.rendering = [rendering]

print(manifest.json(indent=2))
