from ..prezi3_skeletons import Manifest
from ..prezi3_loader import monkeypatch_schema


class MyExtension():
    extension_property = "Example extension property"


monkeypatch_schema(Manifest, MyExtension)
