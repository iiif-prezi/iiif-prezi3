from iiif_prezi3 import Collection, Manifest, ResourceItem, config
from datetime import datetime, timezone

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
base_url = "https://iiif.io/api/cookbook/recipe/0230-navdate"

# n.b: You MUST set `tzinfo` as the Prezi3 Specification requires a timezone, and the default `datetime` does not have one.
manifest1986 = Manifest(id=f"{base_url}/navdate_map_2-manifest.json",
                        label="1986 Chesapeake and Ohio Canal, Washington, D.C., Maryland, West Virginia, official map and guide",
                        navDate=datetime(1986, 1, 1, tzinfo=timezone.utc))
canvas1986 = manifest1986.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/43153e2ec7531f14dd1c9b2fc401678a-87691274-1986",
                                                id=f"{base_url}/canvas/p1",
                                                label="1986 Map, recto and verso, with a date of publication",
                                                anno_id=f"{base_url}/annotation/p0001-image",
                                                anno_page_id=f"{base_url}/page/p1/1")

manifest1987 = Manifest(id=f"{base_url}/navdate_map_1-manifest.json",
                        label="1987 Chesapeake and Ohio Canal, Washington, D.C., Maryland, West Virginia, official map and guide",
                        navDate=datetime(1987, 1, 1, tzinfo=timezone.utc))
canvas1987 = manifest1987.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/43153e2ec7531f14dd1c9b2fc401678a-88695674",
                                                id=f"{base_url}/canvas/p1",
                                                label="1987 Map, recto and verso, with a date of publication",
                                                anno_id=f"{base_url}/annotation/p0001-image",
                                                anno_page_id=f"{base_url}/page/p1/1")

collection = Collection(id=f"{base_url}/navdate-collection.json",
                        label="Chesapeake and Ohio Canal map and guide pamphlets")
thumbnail = ResourceItem(id="https://iiif.io/api/image/3.0/example/reference/43153e2ec7531f14dd1c9b2fc401678a-88695674/full/max/0/default.jpg",
                         type="Image",
                         format="image/jpeg",
                         height=300,
                         width=221)
thumbnail.make_service(id="https://iiif.io/api/image/3.0/example/reference/43153e2ec7531f14dd1c9b2fc401678a-88695674",
                       type="ImageService3",
                       profile="level1")
collection.thumbnail = [thumbnail]

collection.add_item(manifest1986)
collection.add_item(manifest1987)
collection.items[0].navDate = manifest1986.navDate
collection.items[1].navDate = manifest1987.navDate

print(collection.json(indent=2))
