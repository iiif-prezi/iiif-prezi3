# Internationalization and Multi-language Values
### Recipe: [https://iiif.io/api/cookbook/recipe/0006-text-language/](https://iiif.io/api/cookbook/recipe/0006-text-language/)
### JSON-LD: [https://iiif.io/api/cookbook/recipe/0006-text-language/manifest.json](https://iiif.io/api/cookbook/recipe/0006-text-language/manifest.json)

## Method 1 - Construct the language dictionaries during object creation
```python
from iiif_prezi3 import Manifest, KeyValueString

manifest = Manifest(id="https://iiif.io/api/cookbook/recipe/0006-text-language/manifest.json",
                    label={"en": ["Whistler's Mother"], "fr": ["La Mère de Whistler"]})
manifest.metadata = [
    KeyValueString(label={"en": ["Creator"], "fr": ["Auteur"]}, value="Whistler, James Abbott McNeill"),
    KeyValueString(label={"en": ["Subject"], "fr": ["Sujet"]},
                   value={"en": ["McNeill Anna Matilda, mother of Whistler (1804-1881)"],
                          "fr": ["McNeill Anna Matilda, mère de Whistler (1804-1881)"]})
]
manifest.summary = {"en": ["Arrangement in Grey and Black No. 1, also called Portrait of the Artist's Mother."],
                    "fr": ["Arrangement en gris et noir n°1, also called Portrait de la mère de l'artiste."]}
manifest.requiredStatement = KeyValueString(label={"en": ["Held By"], "fr": ["Détenu par"]}, value="Musée d'Orsay, Paris, France")

canvas = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/329817fc8a251a01c393f517d8a17d87-Whistlers_Mother",
                                        id="https://iiif.io/api/cookbook/recipe/0006-text-language/canvas/p1")
canvas.items[0].id = "https://iiif.io/api/cookbook/recipe/0006-text-language/page/p1/1"
canvas.items[0].items[0].id = "https://iiif.io/api/cookbook/recipe/0006-text-language/annotation/p0001-image"

print(manifest.json(indent=2))
```
