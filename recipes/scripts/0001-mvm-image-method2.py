from iiif_prezi3 import Manifest, Canvas, AnnotationPage, Annotation, AnnotationBody, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
base_url = "https://iiif.io/api/cookbook/recipe/0001-mvm-image"

manifest = Manifest(id=f"{base_url}/manifest.json", label="Single Image Example")
canvas = Canvas(id=f"{base_url}/canvas/p1", height=1800, width=1200)
anno_body = AnnotationBody(id="http://iiif.io/api/presentation/2.1/example/fixtures/resources/page1-full.png",
                         type="Image",
                         format="image/png",
                         height=1800,
                         width=1200)
anno_page = AnnotationPage(id=f"{base_url}/page/p1/1")
anno = Annotation(id=f"{base_url}/annotation/p0001-image",
                  motivation="painting",
                  body=anno_body,
                  target=canvas.id)
anno_page.add_item(anno)
canvas.add_item(anno_page)
manifest.add_item(canvas)

print(manifest.json(indent=2))
