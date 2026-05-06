from iiif_prezi3 import Manifest, AnnotationBody, AnnotationPage, Annotation, config, Choice

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
base_url = "https://iiif.io/api/cookbook/recipe/0434-choice-av"

manifest = Manifest(
    id=f"{base_url}/manifest.json",
    label="Excerpt from Egbe Iyawo",
    summary="Excerpt from a performance of Egbe Iyawo recorded in Kabba Division, Kwara State. ",
    rights="http://creativecommons.org/publicdomain/zero/1.0/",
)

canvas = manifest.make_canvas(id=f"{base_url}/canvas/1", duration=16.0)

alac = AnnotationBody(
    id="https://fixtures.iiif.io/audio/ucla/egbe-iyawo-ucla.m4a",
    type="Sound",
    format="audio/alac",
    duration=16.0,
    label="ALAC",
)
mp3 = AnnotationBody(
    id="https://fixtures.iiif.io/audio/ucla/egbe-iyawo-ucla.mp3",
    type="Sound",
    format="audio/mpeg",
    duration=16.0,
    label="MP3",
)
flac = AnnotationBody(
    id="https://fixtures.iiif.io/audio/ucla/egbe-iyawo-ucla.flac",
    type="Sound",
    format="audio/flac",
    duration=16.0,
    label="FLAC",
)
ogg = AnnotationBody(
    id="https://fixtures.iiif.io/audio/ucla/egbe-iyawo-ucla.ogg",
    type="Sound",
    format="audio/ogg",
    duration=16.0,
    label="OGG Vorbis OGG",
)
mpeg2 = AnnotationBody(
    id="https://fixtures.iiif.io/audio/ucla/egbe-iyawo-ucla.mpeg",
    type="Sound",
    format="audio/mpeg",
    duration=16.0,
    label="MPEG2",
)
wav = AnnotationBody(
    id="https://fixtures.iiif.io/audio/ucla/egbe-iyawo-ucla.wav",
    type="Sound",
    format="audio/wav",
    duration=16.0,
    label="WAV",
)

choice = Choice(items=[alac, mp3, flac, ogg, mpeg2, wav])

anno_page = AnnotationPage(id=f"{base_url}/canvas/1/annotation_page/1")
anno = Annotation(
    id=f"{base_url}/canvas/1/annotation_page/1/annotation/1",
    motivation="painting",
    body=choice,
    target=canvas.id,
)
anno_page.add_item(anno)
canvas.add_item(anno_page)

print(manifest.json(indent=2))
