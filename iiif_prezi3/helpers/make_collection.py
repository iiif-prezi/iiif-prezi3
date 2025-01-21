from ..loader import monkeypatch_schema
from ..skeleton import Collection, CollectionRef


class MakeCollection:

    def make_collection(self, **kwargs):
        """Creates a Collection or CollectionRef.

        Creates a new collection, adds it to the calling Collection `items`
        and returns the newly created object. Accepts keyword arguments to
        customize the resulting instance.
        """
        if 'items' not in kwargs:
            child_collection = CollectionRef(**kwargs)
        elif not kwargs['items']:
            kwargs.pop('items')
            child_collection = CollectionRef(**kwargs)
        else:
            child_collection = Collection(**kwargs)
        self.add_item(child_collection)
        return child_collection


monkeypatch_schema(Collection, MakeCollection)
