from ..skeleton import Collection
from ..loader import monkeypatch_schema


class MakeCollection:

    def make_collection(self, **kwargs):
        child_collection = Collection(**kwargs)
        self.add_item(child_collection)
        return child_collection


monkeypatch_schema(Collection, MakeCollection)
