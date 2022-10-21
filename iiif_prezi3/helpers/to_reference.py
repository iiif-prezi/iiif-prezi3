from ..loader import monkeypatch_schema
from ..skeleton import (Annotation, AnnotationCollection, AnnotationPage,
                        Canvas, CanvasRef, Collection, CollectionRef, Manifest,
                        ManifestRef, Range, RangeRef, Reference)


class ToReference:

    def to_reference(self):
        """Returns a Reference object that points to the calling object."""
        # Only try to set thumbnail if it's a Class that can have one
        if isinstance(self, (Collection, Manifest, Canvas, AnnotationPage, Annotation, AnnotationCollection, Range)):
            thumbnail = self.thumbnail
        else:
            thumbnail = None

        # Currently the skeleton Reference requires a label, but some Referenceable objects may not have one (e.g AnnotationPage)
        # TODO: Remove this when the Schema is updated to have different reference types
        if not self.label:
            self.label = ""

        # Ensure that we use a specific Reference type if it exists
        if isinstance(self, Manifest):
            target_type = ManifestRef
        elif isinstance(self, Collection):
            target_type = CollectionRef
        elif isinstance(self, Canvas):
            target_type = CanvasRef
        elif isinstance(self, Range):
            target_type = RangeRef
        else:
            target_type = Reference

        return target_type(id=self.id, label=self.label, type=self.type, thumbnail=thumbnail)


monkeypatch_schema([Manifest, AnnotationPage, Collection, AnnotationCollection, Canvas, Range], ToReference)
