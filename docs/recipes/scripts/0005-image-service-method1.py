from iiif_prezi3 import Manifest, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"

manifest = Manifest(id="https://iiif.io/api/cookbook/recipe/0005-image-service/manifest.json", label="Picture of Göttingen taken during the 2019 IIIF Conference")
canvas = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/918ecd18c2592080851777620de9bcb5-gottingen",
                                        id="https://iiif.io/api/cookbook/recipe/0005-image-service/canvas/p1",
                                        label="Canvas with a single IIIF image")
canvas.items[0].id = "https://iiif.io/api/cookbook/recipe/0005-image-service/page/p1/1"
canvas.items[0].items[0].id = "https://iiif.io/api/cookbook/recipe/0005-image-service/annotation/p0001-image"

print(manifest.json(indent=2))
