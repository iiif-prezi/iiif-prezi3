from iiif_prezi3 import Collection, ManifestRef, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "jp"
base_url = "https://iiif.io/api/cookbook/recipe/0030-multi-volume"

collection = Collection(
    id=f"{base_url}/collection.json",
    label="青楼絵本年中行事 [Seirō ehon nenjū gyōji]",
    behavior=["multi-part"],
)

collection.add_item(
    ManifestRef(
        id=f"{base_url}/manifest_v1.json",
        type="Manifest",
        label="巻 1 [Vol. 1]",
    )
)

collection.add_item(
    ManifestRef(
        id=f"{base_url}/manifest_v2.json",
        type="Manifest",
        label="巻 2 [Vol. 2]",
    )
)

print(collection.json(indent=2))
