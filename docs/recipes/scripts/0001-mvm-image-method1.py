from iiif_prezi3 import Manifest, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"

manifest = Manifest(id="https://iiif.io/api/cookbook/recipe/0001-mvm-image/manifest.json", label="Image 1")
canvas = manifest.make_canvas(id="https://iiif.io/api/cookbook/recipe/0001-mvm-image/canvas/p1", height=1800, width=1200)
anno_page = canvas.add_image(image_url="http://iiif.io/api/presentation/2.1/example/fixtures/resources/page1-full.png",
                             anno_page_id="https://iiif.io/api/cookbook/recipe/0001-mvm-image/page/p1/1",
                             anno_id="https://iiif.io/api/cookbook/recipe/0001-mvm-image/annotation/p0001-image",
                             format="image/png",
                             height=1800,
                             width=1200
                             )

print(manifest.json(indent=2))
