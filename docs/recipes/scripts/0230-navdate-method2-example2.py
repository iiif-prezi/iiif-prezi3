from iiif_prezi3 import Manifest, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"

manifest = Manifest(id="https://iiif.io/api/cookbook/recipe/0230-navdate/navdate_map_1-manifest.json",
                    label="1987 Chesapeake and Ohio Canal, Washington, D.C., Maryland, West Virginia, official map and guide",
                    navDate="1987-01-01T00:00:00Z")
canvas = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/43153e2ec7531f14dd1c9b2fc401678a-88695674",
                                        id="https://iiif.io/api/cookbook/recipe/0230-navdate/canvas/p1",
                                        label="1987 Map, recto and verso, with a date of publication",
                                        anno_id="https://iiif.io/api/cookbook/recipe/0230-navdate/annotation/p0001-image",
                                        anno_page_id="https://iiif.io/api/cookbook/recipe/0230-navdate/page/p1/1")

# This is a workaround for an inconsistency in the Cookbook JSON - see https://github.com/IIIF/cookbook-recipes/issues/376
canvas.items[0].items[0].body.service[0].id = "https://iiif.io/api/image/3.0/example/reference/43153e2ec7531f14dd1c9b2fc401678a-88695674/"

print(manifest.json(indent=2))
