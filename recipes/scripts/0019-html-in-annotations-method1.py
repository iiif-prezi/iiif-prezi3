from iiif_prezi3 import Manifest

manifest = Manifest(id="https://iiif.io/api/cookbook/recipe/0019-html-in-annotations/manifest.json",
                    label={"en": ["Picture of Göttingen taken during the 2019 IIIF Conference"]})
canvas = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/918ecd18c2592080851777620de9bcb5-gottingen",
                                        id="https://iiif.io/api/cookbook/recipe/0019-html-in-annotations/canvas-1",
                                        anno_id="https://iiif.io/api/cookbook/recipe/0019-html-in-annotations/canvas-1/annopage-1/anno-1",
                                        anno_page_id="https://iiif.io/api/cookbook/recipe/0019-html-in-annotations/canvas-1/annopage-1")

anno = canvas.make_annotation(id="https://iiif.io/api/cookbook/recipe/0019-html-in-annotations/canvas-1/annopage-2/anno-1",
                              motivation="commenting",
                              body={"type": "TextualBody",
                                    "language": "de",
                                    "format": "text/html",
                                    "value": "<p>Göttinger Marktplatz mit <a href='https://de.wikipedia.org/wiki/G%C3%A4nseliesel-Brunnen_(G%C3%B6ttingen)'>Gänseliesel Brunnen <img src='https://en.wikipedia.org/static/images/project-logos/enwiki.png' alt='Wikipedia logo'></a></p>"},
                              target=canvas.id,
                              anno_page_id="https://iiif.io/api/cookbook/recipe/0019-html-in-annotations/canvas-1/annopage-2")

print(manifest.json(indent=2))
