from ..skeleton import Collection, Manifest, Canvas, Range, KeyValueString
from ..loader import monkeypatch_schema

class AddMetadata:
    def add_metadata(self, label, value):
        if not self.metadata:
            self.metadata = []
        kv = KeyValueString(label=label, value=value)
        self.metadata.append(kv)

monkeypatch_schema([Collection, Manifest, Canvas, Range], AddMetadata)
