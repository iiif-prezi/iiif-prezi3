from iiif_prezi3 import (Manifest, Provider, Homepage, LinkedResource,
                        AnnotationBody, config)

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
base_url = "https://iiif.io/api/cookbook/recipe/0234-provider"

logo = AnnotationBody(
    id="https://iiif.library.ucla.edu/iiif/2/UCLA-Library-Logo-double-line-2/full/max/0/default.png",
    type="Image",
)
logo.make_service(
    id="https://iiif.library.ucla.edu/iiif/2/UCLA-Library-Logo-double-line-2",
    type="ImageService3",
    profile="level2",
    width=1200,
    height=502,
    sizes=[
        {"width": 300, "height": 126},
        {"width": 600, "height": 251},
        {"width": 1200, "height": 502},
    ],
)

provider = Provider(
    id="https://id.loc.gov/authorities/n79055331",
    label="UCLA Library",
    homepage=
        Homepage(
            id="https://digital.library.ucla.edu/",
            type="Text",
            label="UCLA Library Digital Collections",
            format="text/html",
            language="en",
        )
    ,
    logo=logo,
    seeAlso=
        LinkedResource(
            id="https://id.loc.gov/authorities/names/n79055331.madsxml.xml",
            type="Dataset",
            label="US Library of Congress data about the UCLA Library",
            format="application/xml",
            profile="http://www.loc.gov/mads/v2",
        )
    ,
)

manifest = Manifest(
    id=f"{base_url}/manifest.json",
    label="Playbill Cover",
    summary={
        "en": [
            'Cover of playbill for "Akiba gongen kaisen-banashi," '
            '"Futatsu chōchō kuruwa nikki" and '
            '"Godairiki koi no fūjime" performed at the Chikugo Theater '
            "in Osaka from the fifth month of Kaei 2 (May, 1849); "
            "main actors: Gadō Kataoka II, Ebizō Ichikawa VI, "
            "Kitō Sawamura II, Daigorō Mimasu IV, and Karoku Nakamura I; "
            "on front cover: producer Mominosuke Ichikawa's crest."
        ]
    },
    provider=provider,
)

canvas = manifest.make_canvas_from_iiif(
    url="https://iiif.io/api/image/3.0/example/reference/4f92cceb12dd53b52433425ce44308c7-ucla_bib1987273_no001_rs_001_full",
    id=f"{base_url}/canvas/p0",
    label="front cover with color bar",
    anno_id=f"{base_url}/annotation/p0000-image",
    anno_page_id=f"{base_url}/page/p0/1",
)

print(manifest.json(indent=2))
