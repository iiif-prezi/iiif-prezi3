from iiif_prezi3 import Manifest, config
from datetime import datetime, timezone

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
base_url = "https://iiif.io/api/cookbook/recipe/0230-navdate"

# n.b: You MUST set `tzinfo` as the Prezi3 Specification requires a timezone, and the default `datetime` does not have one.
manifest = Manifest(id=f"{base_url}/navdate_map_2-manifest.json",
                    label="1986 Chesapeake and Ohio Canal, Washington, D.C., Maryland, West Virginia, official map and guide",
                    navDate=datetime(1986, 1, 1, tzinfo=timezone.utc))
canvas = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/43153e2ec7531f14dd1c9b2fc401678a-87691274-1986",
                                        id=f"{base_url}/canvas/p1",
                                        label="1986 Map, recto and verso, with a date of publication",
                                        anno_id=f"{base_url}/annotation/p0001-image",
                                        anno_page_id=f"{base_url}/page/p1/1")

# This is a workaround for an inconsistency in the Cookbook JSON - see https://github.com/IIIF/cookbook-recipes/issues/376
canvas.items[0].items[0].body.service[0].id = "https://iiif.io/api/image/3.0/example/reference/43153e2ec7531f14dd1c9b2fc401678a-87691274-1986/"

print(manifest.json(indent=2))
