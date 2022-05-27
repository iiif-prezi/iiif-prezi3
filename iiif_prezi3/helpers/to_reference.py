from ..loader import monkeypatch_schema
from ..skeleton import Manifest, Reference


class ToReference:

    def to_reference(self):
        """
        Returns a Reference object that points to the calling Manifest
        """
        return Reference(id=self.id, label=self.label, type="Manifest", thumbnail=self.thumbnail)


monkeypatch_schema(Manifest, ToReference)
