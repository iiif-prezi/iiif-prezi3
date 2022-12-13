from ..loader import monkeypatch_schema
from ..skeleton import (Annotation, AnnotationPage, Canvas, Collection,
                        Manifest, Range)


class AnnotationHelpers:

    def add_annotation(self, annotation, anno_page_id=None):
        """Adds the annotation object to the (AnnotationPage object in the) annotations property.

        Creates an AnnotationPage object if it doesn't exist.

        Args:
            annotation (Annotation): the Annotation to add
            anno_page_id (str): An HTTP URL for the annotation page to which the annotation will be attached.

        Returns:
            annotation (Annotation): the Annotation attached to the AnnotationPage.

        """
        if not self.annotations:
            self.annotations = list()

        if len(self.annotations) == 0:
            # add empty AnnotationPage
            anno_page = AnnotationPage(id=anno_page_id, items=[])
            self.annotations.append(anno_page)
        else:
            anno_page = self.annotations[0]

        anno_page.items.append(annotation)

        return annotation

    def make_annotation(self, anno_page_id=None, **kwargs):
        """Creates an annotation object and adds it to the annotations property using .add_annotation().

        Args:
            anno_page_id (str): An HTTP URL for the annotation page to which the annotation will be attached.
            **kwargs (): see Annotation.
        """
        annotation = Annotation(**kwargs)
        self.add_annotation(annotation, anno_page_id=anno_page_id)
        return annotation


monkeypatch_schema([Collection, Manifest, Canvas, Range], AnnotationHelpers)
