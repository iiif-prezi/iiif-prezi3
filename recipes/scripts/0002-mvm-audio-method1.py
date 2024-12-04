from iiif_prezi3 import Manifest, AnnotationPage, Annotation, ResourceItem, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
base_url = "https://iiif.io/api/cookbook/recipe/0002-mvm-audio"

manifest = Manifest(id=f"{base_url}/manifest.json", label="Simplest Audio Example 1")
canvas = manifest.make_canvas(id=f"{base_url}/canvas", duration=1985.024)
anno_body = ResourceItem(id="https://fixtures.iiif.io/audio/indiana/mahler-symphony-3/CD1/medium/128Kbps.mp4",
                         type="Sound",
                         format="audio/mp4",
                         duration=1985.024)
anno_page = AnnotationPage(id=f"{base_url}/canvas/page")
anno = Annotation(id=f"{base_url}/canvas/page/annotation",
                  motivation="painting",
                  body=anno_body,
                  target=canvas.id)
anno_page.add_item(anno)
canvas.add_item(anno_page)

print(manifest.json(indent=2))

