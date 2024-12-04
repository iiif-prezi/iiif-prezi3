from ..loader import monkeypatch_schema
from ..skeleton import (AccompanyingCanvas, Annotation, AnnotationCollection,
                        AnnotationPage, Canvas, Collection, Manifest,
                        PlaceholderCanvas, Range, Reference, ResourceItem, ServiceItem, ServiceItem1)


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
    
    def create_thumbnail_from_iiif(self, url, preferred_width=500, **kwargs):
        """Adds an image thumbnail to a manifest or canvas based on a IIIF service.

        Args:
            url (str): An HTTP URL which points at a IIIF Image response.
            preferred_width (int, optional): the preferred width of the thumbnail.
            **kwargs (): see ResourceItem.

        Returns:
            list[ResourceItem]: The updated list of thumbnails, including the newly-created one.
        """
        image_response = ResourceItem(id=url, type='Image')
        image_info = image_response.set_hwd_from_iiif(url)
        context = image_info.get('@context', '')

        if 'sizes' in image_info:
            best_fit_size = min(
                image_info['sizes'], key=lambda size: abs(size["width"] - preferred_width)
            )
            thumbnail_id = f"{url.replace('/info.json', '')}/full/{best_fit_size['width']},{best_fit_size['height']}/0/default.jpg"
        else:
            thumbnail_id = f"{url.replace('/info.json', '')}/full/full/0/default.jpg" if context == "http://iiif.io/api/image/2/context.json" else f"{url.replace('/info.json', '')}/full/max/0/default.jpg"

        if context == "http://iiif.io/api/image/2/context.json":
            profile = next((item for item in image_info.get('profile', []) if isinstance(item, str)), '')
            service = ServiceItem1(
                id=image_info['@id'],
                profile=profile,
                type="ImageService2",
                format="image/jpeg"
            )
        else:
            service = ServiceItem(
                id=image_info['id'],
                profile=image_info.get('profile', ''),
                type=image_info.get('type', 'ImageService'),
                format="image/jpeg"
            )

        new_thumbnail = ResourceItem(
            id=thumbnail_id,
            type='Image',
            format="image/jpeg",
            **kwargs
        )

        if 'sizes' in image_info:
            new_thumbnail.height = best_fit_size.get('height')
            new_thumbnail.width = best_fit_size.get('width')

        if not hasattr(self, 'thumbnail') or self.thumbnail is None:
            self.thumbnail = []

        new_thumbnail.add_service(service)
        self.thumbnail.append(new_thumbnail)

        return self.thumbnail


monkeypatch_schema([Canvas, PlaceholderCanvas, AccompanyingCanvas, AnnotationPage, Collection, Manifest, Annotation, Range, ResourceItem, AnnotationCollection, Reference], AddThumbnail)
