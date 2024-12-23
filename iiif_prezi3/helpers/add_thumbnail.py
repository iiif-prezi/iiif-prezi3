from ..loader import monkeypatch_schema
from ..skeleton import (AccompanyingCanvas, Annotation, AnnotationCollection,
                        AnnotationPage, Canvas, Collection, Manifest,
                        PlaceholderCanvas, Range, Reference, ResourceItem,
                        ServiceItem, ServiceItem1)


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

        If there is a sizes property, it returns the thumbnail that is closest to the preferred width but larger. If no
        sizes property exists and it's not level zero image service, it returns a thumbnail with the exact preferred
        width. Else, it returns the level `full/full` or `full/max`.

        Args:
            url (str): An HTTP URL which points at a IIIF Image response.
            preferred_width (int, optional): the preferred width of the thumbnail.
            **kwargs (): see ResourceItem.

        Returns:
            new_thumbnail (ResourceItem): The updated list of thumbnails, including the newly-created one.
        """
        image_response = ResourceItem(id=url, type='Image')
        image_info = image_response.set_hwd_from_iiif(url)
        context = image_info.get('@context', '')
        aspect_ratio = image_info.get('width') / image_info.get('height')

        if 'sizes' in image_info:
            best_fit_size = min(
                (size for size in image_info['sizes'] if size["width"] >= preferred_width),
                key=lambda size: size["width"],
                default=image_info['sizes'][-1]
            )
            thumbnail_id = f"{url.replace('/info.json', '')}/full/{best_fit_size['width']},{best_fit_size['height']}/0/default.jpg"
        else:
            # Set a default thumbnail in case of level 0 with no size property
            thumbnail_id = f"{url.replace('/info.json', '')}/full/full/0/default.jpg" if context == "http://iiif.io/api/image/2/context.json" else f"{url.replace('/info.json', '')}/full/max/0/default.jpg"

        if context == "http://iiif.io/api/image/2/context.json":
            profile_data = image_info.get('profile', [])
            if isinstance(profile_data, str):
                profile = profile_data
            elif isinstance(profile_data, list):
                profile = next((item for item in profile_data if isinstance(item, str)), '')
            else:
                profile = ''
            service = ServiceItem1(
                id=image_info['@id'],
                profile=profile,
                type="ImageService2",
                format="image/jpeg"
            )
            if profile == "http://iiif.io/api/image/2/level0.json" and 'sizes' in image_info:
                thumbnail_id = f"{url.replace('/info.json', '')}/full/{best_fit_size['width']},/0/default.jpg"
            elif profile != "http://iiif.io/api/image/2/level0.json" and 'sizes' not in image_info:
                thumbnail_id = f"{url.replace('/info.json', '')}/full/{preferred_width},/0/default.jpg"
        else:
            profile = image_info.get('profile', '')
            service = ServiceItem(
                id=image_info['id'],
                profile=profile,
                type=image_info.get('type', 'ImageService'),
                format="image/jpeg"
            )
            if profile != "level0" and 'sizes' not in image_info:
                thumbnail_id = f"{url.replace('/info.json', '')}/full/{preferred_width},{int(preferred_width/aspect_ratio)}/0/default.jpg"

        new_thumbnail = ResourceItem(
            id=thumbnail_id,
            type='Image',
            format="image/jpeg",
            **kwargs
        )
        if 'sizes' in image_info:
            new_thumbnail.height = best_fit_size.get('height')
            new_thumbnail.width = best_fit_size.get('width')
        elif profile != "http://iiif.io/api/image/2/level0.json" or 'profile' != "level0":
            new_thumbnail.width = preferred_width
            new_thumbnail.height = preferred_width/aspect_ratio
        else:
            new_thumbnail.height = image_info['height']
            new_thumbnail.width = image_info['width']

        if not hasattr(self, 'thumbnail') or self.thumbnail is None:
            self.thumbnail = []

        new_thumbnail.add_service(service)
        self.thumbnail.append(new_thumbnail)

        return self.thumbnail


monkeypatch_schema(
    [Canvas, PlaceholderCanvas, AccompanyingCanvas, AnnotationPage, Collection, Manifest, Annotation,
     Range, ResourceItem, AnnotationCollection, Reference],
    AddThumbnail
)
