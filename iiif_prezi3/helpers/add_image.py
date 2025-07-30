from ..loader import monkeypatch_schema
from ..skeleton import (AccompanyingCanvas, Annotation, AnnotationPage, Canvas,
                        PlaceholderCanvas, AnnotationBody)


class AddImage:

    def add_image(self, image_url, anno_id=None, anno_page_id=None, **kwargs):
        """Adds an image to an existing canvas.

        Args:
            image_url (str): An HTTP URL which points to the image.
            anno_id (str): An HTTP URL for the annotation to which the image will be attached.
            anno_page_id (str): An HTTP URL for the annotation page to which the annotation will be attached.

        Returns:
            anno_page (AnnotationPage): the AnnotationPage with an Annotation and AnnotationBody attached.
        """
        body = AnnotationBody(id=image_url, type='Image', **kwargs)
        annotation = Annotation(id=anno_id, body=body, target=self.id, motivation='painting', type='Annotation')
        anno_page = AnnotationPage(id=anno_page_id, type='AnnotationPage', items=[annotation])
        if not self.items:
            self.items = list()
        self.items.append(anno_page)
        return anno_page


monkeypatch_schema([Canvas, AccompanyingCanvas, PlaceholderCanvas], AddImage)
