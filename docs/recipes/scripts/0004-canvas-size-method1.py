from iiif_prezi3 import Manifest, AnnotationPage, Annotation, ResourceItem, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
base_url = "https://iiif.io/api/cookbook/recipe/0004-canvas-size"

manifest = Manifest(id=f"{base_url}/manifest.json", label="Still image from an opera performance at Indiana University")
canvas = manifest.make_canvas(id=f"{base_url}/canvas/p1")
anno_body = ResourceItem(id="https://fixtures.iiif.io/video/indiana/donizetti-elixir/act1-thumbnail.png",
                         type="Image",
                         format="image/png")
anno_page = AnnotationPage(id=f"{base_url}/page/p1/1")
anno = Annotation(id=f"{base_url}/annotation/p0001-image",
                  motivation="painting",
                  body=anno_body,
                  target=canvas.id)

anno_body.set_hwd(height=360, width=640)
canvas.set_hwd(height=1080, width=1920)

anno_page.add_item(anno)
canvas.add_item(anno_page)

print(manifest.json(indent=2))
