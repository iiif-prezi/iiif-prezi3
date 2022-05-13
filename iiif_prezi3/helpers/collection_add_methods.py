from ..loader import monkeypatch_schema
from ..skeleton import Collection, Reference


class AddToCollection:
    def add_manifest_reference_to_items(self, manifest_id, label):
        manifestref = Reference(id=manifest_id, type="Manifest", label=label)
        if self.items is None:
            self.items = list()
        self.items.append(manifestref)
        return manifestref


monkeypatch_schema(Collection, [AddToCollection])
