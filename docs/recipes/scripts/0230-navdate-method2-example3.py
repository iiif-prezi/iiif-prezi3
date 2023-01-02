from iiif_prezi3 import Collection, ManifestRef, ResourceItem, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"

collection = Collection(id="https://iiif.io/api/cookbook/recipe/0230-navdate/navdate-collection.json",
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

manifest1986 = ManifestRef(id="https://iiif.io/api/cookbook/recipe/0230-navdate/navdate_map_2-manifest.json",
                           type="Manifest",
                           label="1986 Chesapeake and Ohio Canal, Washington, D.C., Maryland, West Virginia, official map and guide",
                           navDate="1986-01-01T00:00:00+00:00")

manifest1987 = ManifestRef(id="https://iiif.io/api/cookbook/recipe/0230-navdate/navdate_map_1-manifest.json",
                           type="Manifest",
                           label="1987 Chesapeake and Ohio Canal, Washington, D.C., Maryland, West Virginia, official map and guide",
                           navDate="1987-01-01T00:00:00+00:00")

collection.add_item(manifest1986)
collection.add_item(manifest1987)

print(collection.json(indent=2))
