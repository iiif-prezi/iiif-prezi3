from ..loader import monkeypatch_schema
from ..skeleton import Canvas, Collection, KeyValueString, Manifest, Range


class AddMetadata:
    def add_metadata(self, label, value):
        if not self.metadata:
            self.metadata = []
        kv = KeyValueString(label=label, value=value)
        self.metadata.append(kv)


monkeypatch_schema([Collection, Manifest, Canvas, Range], AddMetadata)
