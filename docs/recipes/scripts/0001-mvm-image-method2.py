from iiif_prezi3 import Manifest, Canvas, AnnotationPage, Annotation, ResourceItem, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"

manifest = Manifest(id="https://iiif.io/api/cookbook/recipe/0001-mvm-image/manifest.json", label="Image 1")
canvas = Canvas(id="https://iiif.io/api/cookbook/recipe/0001-mvm-image/canvas/p1", height=1800, width=1200)
anno_body = ResourceItem(id="http://iiif.io/api/presentation/2.1/example/fixtures/resources/page1-full.png",
                         type="Image",
                         format="image/png",
                         height=1800,
                         width=1200)
anno_page = AnnotationPage(id="https://iiif.io/api/cookbook/recipe/0001-mvm-image/page/p1/1")
anno = Annotation(id="https://iiif.io/api/cookbook/recipe/0001-mvm-image/annotation/p0001-image",
                  motivation="painting",
                  body=anno_body,
                  target=canvas.id)
anno_page.add_item(anno)
canvas.add_item(anno_page)
manifest.add_item(canvas)

print(manifest.json(indent=2))
