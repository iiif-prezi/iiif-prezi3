from ..skeleton import Manifest, Range
from ..loader import monkeypatch_schema

class AddRange:
    def add_range(self, range):
        if not self.structures:
            self.structures = []
        r = Range(range)
        self.metadata.append(r)

monkeypatch_schema(Manifest, AddRange)
