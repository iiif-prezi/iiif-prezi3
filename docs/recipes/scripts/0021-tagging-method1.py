from iiif_prezi3 import Manifest

base_url = "https://iiif.io/api/cookbook/recipe/0021-tagging"

manifest = Manifest(id=f"{base_url}/manifest.json",
                    label={"en": ["Picture of Göttingen taken during the 2019 IIIF Conference"]})
canvas = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/918ecd18c2592080851777620de9bcb5-gottingen",
                                        id=f"{base_url}/canvas/p1",
                                        anno_id=f"{base_url}/annotation/p0001-image",
                                        anno_page_id=f"{base_url}/page/p1/1")

anno = canvas.make_annotation(id=f"{base_url}/annotation/p0002-tag",
                              motivation="tagging",
                              body={"type": "TextualBody",
                                    "language": "de",
                                    "format": "text/plain",
                                    "value": "Gänseliesel-Brunnen"},
                              target=canvas.id + "#xywh=265,661,1260,1239",
                              anno_page_id=f"{base_url}/page/p2/1")

print(manifest.json(indent=2))
