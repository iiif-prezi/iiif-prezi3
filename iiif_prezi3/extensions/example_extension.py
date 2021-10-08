from ..skeleton import Manifest
from ..loader import monkeypatch_schema


class MyExtension():
    extension_property = "Example extension property"


monkeypatch_schema(Manifest, MyExtension)
