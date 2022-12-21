from ..loader import monkeypatch_schema
from ..skeleton import Annotation, AnnotationPage, Canvas, ResourceItem


class CanvasHelpers:

    def add_image(self, image_url, anno_id=None, anno_page_id=None, **kwargs):
        """Adds an image to an existing canvas.

        Args:
            image_url (str): An HTTP URL which points to the image.
            anno_id (str): An HTTP URL for the annotation to which the image will be attached.
            anno_page_id (str): An HTTP URL for the annotation page to which the annotation will be attached.

        Returns:
            anno_page (AnnotationPage): the AnnotationPage with an Annotation and ResourceItem attached.
        """
        body = ResourceItem(id=image_url, type='Image', **kwargs)
        annotation = Annotation(id=anno_id, body=body, target=self.id, motivation='painting', type='Annotation')
        anno_page = AnnotationPage(id=anno_page_id, type='AnnotationPage', items=[annotation])
        if not self.items:
            self.items = list()
        self.items.append(anno_page)
        return anno_page

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


monkeypatch_schema(Canvas, CanvasHelpers)
