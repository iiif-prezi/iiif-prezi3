from ..loader import monkeypatch_schema
from ..skeleton import (Annotation, AnnotationCollection, AnnotationPage,
                        Canvas, Collection, Manifest, Range, Resource,
                        AnnotationBody, ServiceV3, ServiceV2)


class MakeService:
    def make_service(self, id, type, version=3, **kwargs):
        """Make a IIIF Prezi service of the desired IIIF API version and adds it to the service list.

        Args:
            id (AnyUrl): The id of the service.
            type (str): The type of the service.
            version (int): The API version of the service. Defaults to 3.
            **kwargs (): Arbitrary keyword arguments.

        Raises:
            ValueError: If an invalid IIIF API version is provided.

        Returns:
           service (Union[ServiceV3, ServiceV2]): A service instance of the selected version.
        """
        serviceversions = {
            2: ServiceV2,
            3: ServiceV3
        }
        if version not in serviceversions:
            raise ValueError(f"Version: {version} is not a valid IIIF API service version.")
        service = serviceversions[version](id=id, type=type, **kwargs)
        self.add_service(service)
        return service


monkeypatch_schema([Collection, Manifest, Canvas, Range, Annotation, AnnotationPage, AnnotationCollection, Resource, AnnotationBody], MakeService)
