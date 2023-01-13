from iiif_prezi3 import Manifest, KeyValueString, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"

manifest = Manifest(id="https://iiif.io/api/cookbook/recipe/0008-rights/manifest.json",
                    label="Picture of Göttingen taken during the 2019 IIIF Conference",
                    summary="<p>Picture taken by the <a href=\"https://github.com/glenrobson\">IIIF Technical Coordinator</a></p>",
                    rights="http://creativecommons.org/licenses/by-sa/3.0/",
                    requiredStatement=KeyValueString(label="Attribution",
                                                     value="<span>Glen Robson, IIIF Technical Coordinator. <a href=\"https://creativecommons.org/licenses/by-sa/3.0\">CC BY-SA 3.0</a> <a href=\"https://creativecommons.org/licenses/by-sa/3.0\" title\"CC BY-SA 3.0\"><img src=\"https://licensebuttons.net/l/by-sa/3.0/88x31.png\"/></a></span>")
                    )

canvas = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/918ecd18c2592080851777620de9bcb5-gottingen",
                                        id="https://iiif.io/api/cookbook/recipe/0008-rights/canvas/p1",
                                        anno_id="https://iiif.io/api/cookbook/recipe/0008-rights/annotation/p0001-image",
                                        anno_page_id="https://iiif.io/api/cookbook/recipe/0008-rights/page/p1/1")

print(manifest.json(indent=2))
