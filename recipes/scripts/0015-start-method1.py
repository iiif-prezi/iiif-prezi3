from iiif_prezi3 import Manifest, KeyValueString, ResourceItem, AnnotationPage, Annotation, SpecificResource, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
manifest = Manifest(id="https://iiif.io/api/cookbook/recipe/0015-start/manifest.json",
                    label="Video of a 30-minute digital clock",
                    rights="http://creativecommons.org/licenses/by/3.0/",
                    requiredStatement=KeyValueString(label="Attribution",
                                                     value="<span>The video was created by <a href='https://www.youtube.com/watch?v=Lsq0FiXjGHg'>DrLex1</a> and was released using a <a href='https://creativecommons.org/licenses/by/3.0/'>Creative Commons Attribution license</a></span>")
                    )

canvas = manifest.make_canvas(id="https://iiif.io/api/cookbook/recipe/0015-start/canvas/segment1", duration=1801.055)
anno_body = ResourceItem(id="https://fixtures.iiif.io/video/indiana/30-minute-clock/medium/30-minute-clock.mp4",
                         type="Video",
                         format="video/mp4",
                         duration=1801.055)
anno_page = AnnotationPage(id="https://iiif.io/api/cookbook/recipe/0015-start/annotation/segment1/page")
anno = Annotation(id="https://iiif.io/api/cookbook/recipe/0015-start/annotation/segment1-video",
                  motivation="painting",
                  body=anno_body,
                  target=canvas.id)

anno_page.add_item(anno)
canvas.add_item(anno_page)

manifest.start = SpecificResource(id="https://iiif.io/api/cookbook/recipe/0015-start/canvas-start/segment1",
                                  source=canvas.id,
                                  selector={"type": "PointSelector", "t": 120.5})

print(manifest.json(indent=2))
