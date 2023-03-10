from ..loader import monkeypatch_schema
from ..skeleton import (AccompanyingCanvas, Annotation, AnnotationCollection,
                        AnnotationPage, Canvas, Collection, Manifest,
                        PlaceholderCanvas, Range, Reference, ResourceItem)


class AddThumbnail:
    def add_thumbnail(self, image_url, **kwargs):
        """Adds a thumbnail to an existing canvas.

        Args:
            image_url (str): An HTTP URL which points to the thumbnail.
            **kwargs (): see ResourceItem.

        Returns:
            new_thumbnail (ResourceItem): the newly-created thumbnail.
        """
        new_thumbnail = ResourceItem(id=image_url, type='Image', **kwargs)
        if not self.thumbnail:
            self.thumbnail = list()
        self.thumbnail.append(new_thumbnail)
        return new_thumbnail


monkeypatch_schema([Canvas, PlaceholderCanvas, AccompanyingCanvas, AnnotationPage, Collection, Manifest, Annotation, Range, ResourceItem, AnnotationCollection, Reference], AddThumbnail)
