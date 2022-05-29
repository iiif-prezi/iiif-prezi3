from ..loader import monkeypatch_schema
from ..skeleton import (Annotation, AnnotationPage, Canvas, Collection,
                        Manifest, Range)


class AnnotationHelpers:

    def add_annotation(self, annotation):
        """Adds the annotation object to the (AnnotationPage object in the) annotations property.

        Args:
          annotation (iiif-prezi3.Annotation): the Annotation to add

        Creates an AnnotationPage object if it doesn't exist.
        """
        if not self.annotations:
            self.annotations = list()

        if len(self.annotations) == 0:
            # add empty AnnotationPage
            anno_page = AnnotationPage(items=[])
            self.annotations.append(anno_page)
        else:
            anno_page = self.annotations[0]

        anno_page.items.append(annotation)

        return annotation

    def make_annotation(self, **kwargs):
        """Creates an annotation object and adds it to the annotations property using .add_annotation().

        Args: (see iiif-prezi3.Annotation)
        """
        annotation = Annotation(**kwargs)
        self.add_annotation(annotation)
        return annotation


monkeypatch_schema([Collection, Manifest, Canvas, Range], AnnotationHelpers)
