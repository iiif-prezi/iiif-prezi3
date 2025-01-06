from ..loader import monkeypatch_schema
from ..skeleton import (ExternalItem, AnnotationPage, AccompanyingCanvas, Annotation, AnnotationCollection, Canvas,
                        PlaceholderCanvas, Range, ResourceItem, Collection, Manifest)


class AddRendering:
    def add_rendering(self, external_item):
        """Add an external item to a rendering list.

        Args:
            external_item (ExternalItem): An ExternalItem instance.
        """
        if isinstance(external_item, (ExternalItem)):
            if not hasattr(self, 'rendering') or self.rendering is None:
                self.rendering = []
            self.rendering.append(external_item)
            self.rendering = self.rendering
        else:
            raise TypeError("Not a valid ExternalItem instance.")


monkeypatch_schema([ AnnotationPage, AccompanyingCanvas, Annotation, AnnotationCollection, Canvas,
                     PlaceholderCanvas, Range, ResourceItem, Collection, Manifest ], AddRendering)
