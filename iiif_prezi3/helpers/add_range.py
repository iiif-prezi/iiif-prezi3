from ..loader import monkeypatch_schema
from ..skeleton import Manifest


class AddRange:
    def add_range(self, range):
        if not self.structures:
            self.structures = []
        self.structures.append(range)


monkeypatch_schema(Manifest, AddRange)
