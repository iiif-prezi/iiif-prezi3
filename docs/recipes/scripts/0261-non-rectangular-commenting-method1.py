from iiif_prezi3 import Manifest, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
base_url = "https://iiif.io/api/cookbook/recipe/0261-non-rectangular-commenting"

manifest = Manifest(id=f"{base_url}/manifest.json", label="Picture of Göttingen taken during the 2019 IIIF Conference")
canvas = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/918ecd18c2592080851777620de9bcb5-gottingen",
                                        id=f"{base_url}/canvas/p1",
                                        anno_id=f"{base_url}/annotation/p0001-image",
                                        anno_page_id=f"{base_url}/page/p1/1")
anno = canvas.make_annotation(id=f"{base_url}/annotation/p0002-svg",
                              motivation="tagging",
                              body={"type": "TextualBody",
                                    "language": "de",
                                    "format": "text/plain",
                                    "value": "Gänseliesel-Brunnen"},
                              target={"type": "SpecificResource",
                                      "source": canvas.id,
                                      "selector": {"type": "SvgSelector",
                                                   "value": "<svg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'><g><path d='M270.000000,1900.000000 L1530.000000,1900.000000 L1530.000000,1610.000000 L1315.000000,1300.000000 L1200.000000,986.000000 L904.000000,661.000000 L600.000000,986.000000 L500.000000,1300.000000 L270,1630 L270.000000,1900.000000' /></g></svg>"
                                                   }
                                      },
                              anno_page_id=f"{base_url}/page/p2/1")

print(manifest.json(indent=2))
