import unittest
from unittest.mock import Mock, patch

from iiif_prezi3 import Manifest


class CreateCanvasFromIIIFTests(unittest.TestCase):

    def setUp(self):
        self.manifest = Manifest(label={'en': ['Manifest label']})

    @patch('iiif_prezi3.helpers.set_hwd_from_iiif.requests.get')
    def test_create_canvas_from_iiif_v3(self, mockrequest_get):
        image_id = 'https://iiif.io/api/image/3.0/example/reference/918ecd18c2592080851777620de9bcb5-gottingen'
        image_info_url = f'{image_id}/info.json'

        # successful response with dimensions
        mockresponse = Mock(status_code=200)
        mockrequest_get.return_value = mockresponse
        # set mock to return minimal image api response
        mockresponse.json.return_value = {
            "@context": "http://iiif.io/api/image/3/context.json",
            "extraFormats": ["jpg", "png"],
            "extraQualities": ["default", "color", "gray"],
            "height": 3024,
            "id": "https://iiif.io/api/image/3.0/example/reference/918ecd18c2592080851777620de9bcb5-gottingen",
            "profile": "level1",
            "protocol": "http://iiif.io/api/image",
            "tiles": [{
                "height": 512,
                "scaleFactors": [1, 2, 4],
                "width": 512
            }],
            "type": "ImageService3",
            "width": 4032
        }

        canvas = self.manifest.create_canvas_from_iiif(image_info_url, label={'en': ['Canvas label']})

        # Check canvas params made it through
        self.assertEqual(canvas.label,
                         {'en': ['Canvas label']})

        # check canvas dimensions
        self.assertEqual(canvas.height, 3024)
        self.assertEqual(canvas.width, 4032)

        # Check annotation
        annotation = canvas.items[0].items[0]
        self.assertEqual(annotation.motivation, "painting")

        # Check resource
        resource = annotation.body

        self.assertEqual(resource.id, f'{image_id}/full/max/0/default.jpg')
        self.assertEqual(resource.type, 'Image')
        self.assertEqual(resource.format, 'image/jpeg')
        self.assertEqual(resource.height, 3024)
        self.assertEqual(resource.width, 4032)

        # Check service
        service = resource.service[0]

        self.assertEqual(service.id, image_id)
        self.assertEqual(service.profile, "level1")
        self.assertEqual(service.type, "ImageService3")

    @patch('iiif_prezi3.helpers.set_hwd_from_iiif.requests.get')
    def test_create_canvas_from_iiif_v2(self, mockrequest_get):
        image_id = 'https://iiif.io/api/image/2.1/example/reference/918ecd18c2592080851777620de9bcb5-gottingen'
        image_info_url = f'{image_id}/info.json'

        # successful response with dimensions
        mockresponse = Mock(status_code=200)
        mockrequest_get.return_value = mockresponse
        # set mock to return minimal image api response
        mockresponse.json.return_value = {
            "@context": "http://iiif.io/api/image/2/context.json",
            "@id": "https://iiif.io/api/image/2.1/example/reference/918ecd18c2592080851777620de9bcb5-gottingen",
            "height": 3024,
            "profile": [
                "http://iiif.io/api/image/2/level1.json",
                {
                    "formats": ["jpg", "png"],
                    "qualities": ["default", "color", "gray"]
                }
            ],
            "protocol": "http://iiif.io/api/image",
            "tiles": [
                {
                    "height": 512,
                    "scaleFactors": [1, 2, 4],
                    "width": 512
                }
            ],
            "width": 4032
        }

        canvas = self.manifest.create_canvas_from_iiif(image_info_url, label={'en': ['Canvas label']})

        # Check canvas params made it through
        self.assertEqual(canvas.label,
                         {'en': ['Canvas label']})

        # check canvas dimensions
        self.assertEqual(canvas.height, 3024)
        self.assertEqual(canvas.width, 4032)

        # Check annotation
        annotation = canvas.items[0].items[0]
        self.assertEqual(annotation.motivation, "painting")

        # Check resource
        resource = annotation.body

        self.assertEqual(resource.id, f'{image_id}/full/full/0/default.jpg')
        self.assertEqual(resource.type, 'Image')
        self.assertEqual(resource.format, 'image/jpeg')
        self.assertEqual(resource.height, 3024)
        self.assertEqual(resource.width, 4032)

        # Check service
        service = resource.service[0]

        self.assertEqual(service.id, image_id)
        self.assertEqual(service.profile, "http://iiif.io/api/image/2/level1.json")
        self.assertEqual(service.type, "ImageService2")
