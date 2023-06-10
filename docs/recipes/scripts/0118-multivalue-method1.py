from iiif_prezi3 import Manifest, KeyValueString

base_url = "https://iiif.io/api/cookbook/recipe/0118-multivalue"

manifest = Manifest(id="https://iiif.io/api/cookbook/recipe/0118_multivalue/manifest.json",
                    label={"fr": ["Arrangement en gris et noir no 1"]})
manifest.metadata = [
    KeyValueString(label={"en": ["Alternative titles"]},
                   value={"en": ["Whistler's Mother", "Arrangement in Grey and Black No. 1"],
                          "fr": ["Portrait de la mère de l'artiste", "La Mère de Whistler"]})
]
manifest.summary = {"en": ["A painting in oil on canvas created by the American-born painter James McNeill Whistler, in 1871."]}

canvas = manifest.make_canvas(id="https://iiif.io/api/cookbook/recipe/0118_multivalue/canvas/1", height=991, width=1114)
anno_page = canvas.add_image(image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Whistlers_Mother_high_res.jpg/1114px-Whistlers_Mother_high_res.jpg",
                             anno_page_id="https://iiif.io/api/cookbook/recipe/0118_multivalue/canvas/1/page/1",
                             anno_id="https://iiif.io/api/cookbook/recipe/0118_multivalue/canvas/1/page/1/annotation/1",
                             format="image/jpeg",
                             )

canvas.items[0].items[0].id = "https://iiif.io/api/cookbook/recipe/0118_multivalue/canvas/1/page/1/annotation/1"

print(manifest.json(indent=2))
