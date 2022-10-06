from ..loader import monkeypatch_schema
from ..skeleton import Collection


class MakeCollection:

    def make_collection(self, **kwargs):
        """Create a Collection.

        Creates a new collection, adds it to the calling Collection `items`
        and returns the newly created object. Accepts keyword arguments to
        customize the resulting instance.
        """
        child_collection = Collection(**kwargs)
        self.add_item(child_collection)
        return child_collection


monkeypatch_schema(Collection, MakeCollection)
