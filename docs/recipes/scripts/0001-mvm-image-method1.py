from iiif_prezi3 import Manifest, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
base_url = "https://iiif.io/api/cookbook/recipe/0001-mvm-image"

manifest = Manifest(id=f"{base_url}/manifest.json", label="Single Image Example")
canvas = manifest.make_canvas(id=f"{base_url}/canvas/p1", height=1800, width=1200)
anno_page = canvas.add_image(image_url="http://iiif.io/api/presentation/2.1/example/fixtures/resources/page1-full.png",
                             anno_page_id=f"{base_url}/page/p1/1",
                             anno_id=f"{base_url}/annotation/p0001-image",
                             format="image/png",
                             height=1800,
                             width=1200
                             )

print(manifest.json(indent=2))
