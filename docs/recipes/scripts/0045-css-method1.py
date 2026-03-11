from iiif_prezi3 import Manifest, SpecificResource, TextualBody, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
base_url = "https://iiif.io/api/cookbook/recipe/0045-css"

manifest = Manifest(
    id=f"{base_url}/manifest.json",
    label="Koto, chess, calligraphy, and painting",
)
manifest.add_label("琴棋書画図屏風", "ja")

canvas = manifest.make_canvas_from_iiif(
    url="https://iiif.io/api/image/3.0/example/reference/36ca0a3370db128ec984b33d71a1543d-100320001004",
    id=f"{base_url}/canvas/p1",
    anno_id=f"{base_url}/annotation/p0001-image",
    anno_page_id=f"{base_url}/page/p1/1",
)

anno1_body = SpecificResource(
    id=f"{base_url}/body/sr1",
    styleClass="author1note",
    source=TextualBody(
        id=f"{base_url}/body/text1",
        language="en",
        format="text/html",
        value="<p>Three of the four pursuits of refined and noble men named in the screen's title are shown on this side of the screen: go, the koto, and tools for calligraphy. Each is in a container or wrapper. (GR)</p>",
    ),
)

anno1_target = SpecificResource(
    source=f"{base_url}/canvas/p1",
    styleClass="author2highlight",
    selector={"type": "FragmentSelector", "value": "xywh=700,1250,1850,1150"},
)

anno1 = canvas.make_annotation(
    id=f"{base_url}/page/p2/anno-1",
    motivation="commenting",
    stylesheet=f"{base_url}/style.css",
    body=anno1_body,
    target=anno1_target,
    anno_page_id=f"{base_url}/page/p2/1",
)

anno2_body = SpecificResource(
    id=f"{base_url}/body/sr2",
    styleClass="author2note",
    source=TextualBody(
        id=f"{base_url}/body/text2",
        language="en",
        format="text/html",
        value="<p>The detail in the natural beauty of the setting could be seen as a contrast (or balance) to the manufactured pursuits of noble men. (TK)</p>",
    ),
)

anno2_target = SpecificResource(
    source=f"{base_url}/canvas/p1",
    styleClass="author2highlight",
    selector={"type": "FragmentSelector", "value": "xywh=170,160,2200,1000"},
)

anno2 = canvas.make_annotation(
    id=f"{base_url}/page/p2/anno-2",
    motivation="commenting",
    stylesheet=f"{base_url}/style.css",
    body=anno2_body,
    target=anno2_target,
    anno_page_id=f"{base_url}/page/p2/1",
)

print(manifest.json(indent=2))
