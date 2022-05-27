from ..skeleton import Collection
from ..loader import monkeypatch_schema


class MakeCollection:
    """
    Creates a new collection, adds it to the calling Collection `items`
    and returns the newly created object. Accepts keyword arguments to 
    customize the resulting instance.
    """

    def make_collection(self, **kwargs):
        child_collection = Collection(**kwargs)
        self.add_item(child_collection)
        return child_collection


monkeypatch_schema(Collection, MakeCollection)
