
from ..loader import monkeypatch_schema
from ..skeleton import (Annotation, AnnotationPage, Canvas, Manifest,
                        AnnotationBody, ServiceV3, ServiceV2)


class CreateCanvasFromIIIF:
    # should probably be added to canvas helpers

    def create_canvas_from_iiif(self, url, anno_id=None, anno_page_id=None, **kwargs):
        """Create a canvas from a IIIF Image URL.

        Creates a canvas from a IIIF Image service passing any kwargs to the Canvas.

        Args:
            url (str): An HTTP URL at which at a IIIF Image is available.
            anno_id (str): An HTTP URL for the annotation to which the image will be attached.
            anno_page_id (str): An HTTP URL for the annotation page to which the annotation will be attached.
            **kwargs (): see Canvas

        Returns:
            canvas (Canvas): the Canvas created from the IIIF Image.

        """
        canvas = Canvas(**kwargs)

        body = AnnotationBody(id="http://example.com", type="Image")
        infoJson = body.set_hwd_from_iiif(url)

        # Will need to handle IIIF 2...
        if 'type' not in infoJson:
            # Assume v2

            # V2 profile contains profile URI plus extra features
            profile = ''
            for item in infoJson['profile']:
                if isinstance(item, str):
                    profile = item
                    break

            service = ServiceV2(id=infoJson['@id'], profile=profile, type="ImageService2")
            body.service = [service]
            body.id = f'{infoJson["@id"]}/full/full/0/default.jpg'
            body.format = "image/jpeg"
        else:
            service = ServiceV3(id=infoJson['id'], profile=infoJson['profile'], type=infoJson['type'])
            body.service = [service]
            body.id = f'{infoJson["id"]}/full/max/0/default.jpg'
            body.format = "image/jpeg"

        annotation = Annotation(id=anno_id, motivation='painting', body=body, target=canvas.id)

        annotationPage = AnnotationPage(id=anno_page_id)
        annotationPage.add_item(annotation)

        canvas.add_item(annotationPage)
        canvas.set_hwd(infoJson['height'], infoJson['width'])

        return canvas

    def make_canvas_from_iiif(self, url, **kwargs):
        canvas = self.create_canvas_from_iiif(url, **kwargs)

        self.add_item(canvas)
        return canvas


monkeypatch_schema(Manifest, [CreateCanvasFromIIIF])
