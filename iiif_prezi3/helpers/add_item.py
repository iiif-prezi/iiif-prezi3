from ..loader import monkeypatch_schema
from ..skeleton import (AccompanyingCanvas, AnnotationPage, Canvas, Collection,
                        Manifest, PlaceholderCanvas, Range, Reference)


class AddItem:
    def add_item(self, item):
        """Add a IIIF Prezi3 object to the items list, creating it if it doesn't exist.

        Args:
            item (Union[Collection, Manifest, Canvas, AnnotationPage, Annotation, Range, Reference, SpecificResource, Item])): The object to be added
        """
        if not self.items:
            self.items = []

        # If the item is a Manifest, and the target is a Collection, convert it to a reference
        if isinstance(item, Manifest) and isinstance(self, Collection):
            item = item.to_reference()

        self.items.append(item)
        self.items = self.items  # Force Pydantic to validate?


class AddItemByReference:
    def add_item_by_reference(self, item):
        """Add a IIIF Prezi3 object by reference to the items list, creating it if it doesn't exist.

        Args:
            item (Union[Manifest, AnnotationPage, Collection, AnnotationCollection, Canvas])): The object to be added
        """
        if not self.items:
            self.items = []

        item = item.to_reference()

        self.items.append(item)
        self.items = self.items  # Force Pydantic to validate?


monkeypatch_schema([Collection, Manifest, Canvas, Range, AnnotationPage, Reference, AccompanyingCanvas, PlaceholderCanvas], AddItem)
monkeypatch_schema([Collection, Range, Canvas, AnnotationPage, AccompanyingCanvas], AddItemByReference)
