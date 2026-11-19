from ..loader import monkeypatch_schema
from ..skeleton import (AccompanyingCanvas, Canvas, Collection, LinkedResource,
                        Manifest, PlaceholderCanvas, Provider)


class AddSeeAlso:
    def add_see_also(self, linked_resource):
        """Adds a LinkedResource to an existing resource's seeAlso list.

        Args:
            linked_resource (LinkedResource): A LinkedResource instance.
        """
        if isinstance(linked_resource, LinkedResource):
            current = getattr(self, 'seeAlso', None)
            current = getattr(current, 'root', current) or []
            self.seeAlso = [*current, linked_resource]
        else:
            raise TypeError("Not a valid LinkedResource instance.")


monkeypatch_schema(
    [Collection, Manifest, AccompanyingCanvas, Canvas, PlaceholderCanvas, Provider],
    AddSeeAlso
)
