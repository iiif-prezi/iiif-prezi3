from iiif_prezi3 import Manifest, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
base_url = "https://iiif.io/api/cookbook/recipe/0005-image-service"

manifest = Manifest(id=f"{base_url}/manifest.json", label="Picture of Göttingen taken during the 2019 IIIF Conference")
canvas = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/918ecd18c2592080851777620de9bcb5-gottingen",
                                        id=f"{base_url}/canvas/p1",
                                        label="Canvas with a single IIIF image",
                                        anno_id=f"{base_url}/annotation/p0001-image",
                                        anno_page_id=f"{base_url}/page/p1/1")

print(manifest.json(indent=2))
