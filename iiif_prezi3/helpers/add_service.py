from ..loader import monkeypatch_schema
from ..skeleton import (Annotation, AnnotationCollection, AnnotationPage,
                        Canvas, Collection, Manifest, Range, Resource,
                        AnnotationBody, ServiceV3, ServiceV2)


class AddService:
    def add_service(self, service):
        """Add a IIIF Prezi service to the service list.

        Args:
            service (ServiceV3,ServiceV2,Service): A iiif-prezi ServiceV3.
        """
        if isinstance(service, (ServiceV3, ServiceV2)):
            if not self.service:
                self.service = []
            self.service.append(service)
            self.service = self.service
        else:
            raise TypeError("Not a valid IIIF service.")


monkeypatch_schema([Collection, Manifest, Canvas, Range, Annotation, AnnotationPage, AnnotationCollection, Resource, AnnotationBody], AddService)
