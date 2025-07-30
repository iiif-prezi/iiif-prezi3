from ..loader import monkeypatch_schema
from ..skeleton import (AccompanyingCanvas, Annotation, AnnotationCollection,
                        AnnotationPage, Canvas, Collection, Manifest,
                        PlaceholderCanvas, Range, Reference, AnnotationBody,
                        ServiceV3, ServiceV2)


class AddThumbnail:
    def add_thumbnail(self, image_url, **kwargs):
        """Adds a thumbnail to an existing canvas.

        Args:
            image_url (str): An HTTP URL which points to the thumbnail.
            **kwargs (): see AnnotationBody.

        Returns:
            new_thumbnail (AnnotationBody): the newly-created thumbnail.
        """
        new_thumbnail = AnnotationBody(id=image_url, type='Image', **kwargs)
        if not self.thumbnail:
            self.thumbnail = list()
        self.thumbnail.append(new_thumbnail)
        return new_thumbnail

    @staticmethod
    def __get_best_fit_size(image_info, preferred_width):
        if 'sizes' in image_info:
            return min(
                (size for size in image_info['sizes'] if size["width"] >= preferred_width),
                key=lambda size: size["width"],
                default=image_info['sizes'][-1]
            )
        else:
            return None

    @staticmethod
    def __get_profile(image_info):
        profile_data = image_info.get('profile', [''])
        if isinstance(profile_data, list):
            return profile_data[0]
        else:
            return profile_data

    def __get_thumbnail_id(self, url, image_info, best_fit, preferred_width, aspect_ratio):
        context = image_info.get('@context', '')
        profile = self.__get_profile(image_info)
        base_url = url.replace('/info.json', '')
        if best_fit:
            width = best_fit['width']
            height = best_fit.get('height', '')
            if context == "http://iiif.io/api/image/2/context.json":
                return f"{base_url}/full/{width},/0/default.jpg"
            else:
                return f"{base_url}/full/{width},{height}/0/default.jpg"
        if profile not in ("http://iiif.io/api/image/2/level0.json", "level0"):
            if context == "http://iiif.io/api/image/2/context.json":
                return f"{base_url}/full/{preferred_width},/0/default.jpg"
            else:
                height = int(preferred_width / aspect_ratio)
                return f"{base_url}/full/{preferred_width},{height}/0/default.jpg"
        if context == "http://iiif.io/api/image/2/context.json":
            return f"{base_url}/full/full/0/default.jpg"
        else:
            return f"{base_url}/full/max/0/default.jpg"

    def create_thumbnail_from_iiif(self, url, preferred_width=500, **kwargs):
        """Adds an image thumbnail to a manifest or canvas based on a IIIF service.

        If there is a sizes property, it returns the thumbnail that is closest to the preferred width but larger. If no
        sizes property exists and it's not level zero image service, it returns a thumbnail with the exact preferred
        width. Else, it returns the level `full/full` or `full/max`.

        Args:
            url (str): An HTTP URL which points at a IIIF Image response.
            preferred_width (int, optional): the preferred width of the thumbnail.
            **kwargs (): see AnnotationBody.

        Returns:
            new_thumbnail (AnnotationBody): The updated list of thumbnails, including the newly-created one.
        """
        image_response = AnnotationBody(id=url, type='Image')
        image_info = image_response.set_hwd_from_iiif(url)
        context = image_info.get('@context', '')
        aspect_ratio = image_info.get('width') / image_info.get('height')
        profile = self.__get_profile(image_info)
        best_fit_size = self.__get_best_fit_size(image_info, preferred_width)
        thumbnail_id = self.__get_thumbnail_id(url, image_info, best_fit_size, preferred_width, aspect_ratio)

        new_thumbnail = AnnotationBody(id=thumbnail_id, type='Image', format="image/jpeg", **kwargs)
        if best_fit_size:
            new_thumbnail.width = best_fit_size['width']
            new_thumbnail.height = best_fit_size['height']
        else:
            new_thumbnail.width = preferred_width
            new_thumbnail.height = int(preferred_width / aspect_ratio)

        if not hasattr(self, 'thumbnail') or self.thumbnail is None:
            self.thumbnail = []

        service = (
            ServiceV2(
                id=image_info['@id'],
                profile=profile,
                type="ImageService2",
                format="image/jpeg"
            )
            if context == "http://iiif.io/api/image/2/context.json"
            else ServiceV3(
                id=image_info['id'],
                profile=profile,
                type=image_info.get('type', 'ImageService'),
                format="image/jpeg"
            )
        )
        new_thumbnail.add_service(service)
        self.thumbnail.append(new_thumbnail)
        return self.thumbnail


monkeypatch_schema(
    [Canvas, PlaceholderCanvas, AccompanyingCanvas, AnnotationPage, Collection, Manifest, Annotation,
     Range, AnnotationBody, AnnotationCollection, Reference],
    AddThumbnail
)
