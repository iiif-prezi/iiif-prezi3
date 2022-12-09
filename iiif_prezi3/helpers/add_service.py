from ..loader import monkeypatch_schema
from ..skeleton import (Annotation, AnnotationCollection, AnnotationPage,
                        Canvas, Collection, Manifest, Range, Resource,
                        ResourceItem, ServiceItem, ServiceItem1)


class AddService:
    def add_service(self, service):
        """Add a IIIF Prezi service to the service list.

        Args:
            service (ServiceItem,ServiceItem1,Service): A iiif-prezi ServiceItem.
        """
        if isinstance(service, (ServiceItem, ServiceItem1)):
            if not self.service:
                self.service = []
            self.service.append(service)
            self.service = self.service
        else:
            raise TypeError("Not a valid IIIF service.")


monkeypatch_schema([Collection, Manifest, Canvas, Range, Annotation, AnnotationPage, AnnotationCollection, Resource, ResourceItem], AddService)
