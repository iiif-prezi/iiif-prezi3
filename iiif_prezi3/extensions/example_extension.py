from ..loader import monkeypatch_schema
from ..skeleton import Manifest


class MyExtension():
    extension_property = "Example extension property"


monkeypatch_schema(Manifest, MyExtension)
