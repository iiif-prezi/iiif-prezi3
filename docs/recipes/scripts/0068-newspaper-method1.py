from iiif_prezi3 import (Collection, ManifestRef, Provider, AnnotationBody,
                        LinkedResource, KeyValueString, config)

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "none"
base_url = "https://iiif.io/api/cookbook/recipe/0068-newspaper"

logo = AnnotationBody(
    id="https://style.europeana.eu/images/europeana-logo-default.png",
    type="Image",
    format="image/png",
    height=310,
    width=100,
)

collection = Collection(
    id=f"{base_url}/newspaper_title-collection.json",
    label={"de": ["Berliner Tageblatt"]},
    metadata=[
        KeyValueString(
            label={"en": ["type"]},
            value={
                "none": ["http://data.europeana.eu/concept/base/18"],
                "en": ["Newspaper Title", "Serial"],
            },
        ),
        KeyValueString(
            label={"en": ["language"]},
            value={
                "none": ["de"],
                "en": ["German"],
            },
        ),
    ],
    rights="http://creativecommons.org/publicdomain/mark/1.0/",
    requiredStatement=KeyValueString(
        label={"en": ["Attribution"]},
        value={
            "en": [
                "<p><a href='https://www.europeana.eu/portal/record/"
                "9200355/BibliographicResource_3000096302605.html'>"
                "Berliner Tageblatt</a> - Staatsbibliothek zu Berlin"
                " - Preu\u00dfischer Kulturbesitz. Public Domain Mark"
                " - http://creativecommons.org/publicdomain/mark/1.0/</p>"
            ]
        },
    ),
    provider=[
        Provider(
            id="https://www.europeana.eu/",
            label={"en": ["Europeana"]},
            logo=[logo],
        )
    ],
    seeAlso=[
        LinkedResource(
            id="https://www.europeana.eu/api/v2/record/9200355/"
               "BibliographicResource_3000096302605.json-ld",
            type="Dataset",
            format="application/ld+json",
            profile="http://www.europeana.eu/schemas/edm/",
        )
    ],
)

collection.add_item(
    ManifestRef(
        id=f"{base_url}/newspaper_issue_1-manifest.json",
        type="Manifest",
        label={"de": ["Berliner Tageblatt - 1925-02-16"]},
        navDate="1925-02-16T00:00:00Z",
    )
)

collection.add_item(
    ManifestRef(
        id=f"{base_url}/newspaper_issue_2-manifest.json",
        type="Manifest",
        label={"de": ["Berliner Tageblatt - 1925-03-13"]},
        navDate="1925-03-13T00:00:00Z",
    )
)

print(collection.json(indent=2))
