import unittest
from unittest.mock import Mock, patch

from iiif_prezi3 import Manifest


class AddThumbnailTests(unittest.TestCase):

    def setUp(self):
        self.manifest = Manifest(label={'en': ['Manifest label']})

    @patch('iiif_prezi3.helpers.set_hwd_from_iiif.requests.get')
    def test_create_thumbnail_from_iiif_v3(self, mockrequest_get):
        image_id = 'https://fixtures.iiif.io/other/level0/Glen/photos/gottingen'
        image_info_url = f'{image_id}/info.json'

        # successful response with dimensions
        mockresponse = Mock(status_code=200)
        mockrequest_get.return_value = mockresponse
        # set mock to return minimal image api response
        mockresponse.json.return_value = {
            "@context": "http://iiif.io/api/image/3/context.json",
            "id": "https://fixtures.iiif.io/other/level0/Glen/photos/gottingen",
            "type": "ImageService3",
            "protocol": "http://iiif.io/api/image",
            "profile": "level0",
            "width": 4032,
            "height": 3024,
            "sizes": [
                {
                  "width": 126,
                  "height": 95
                },
                {
                    "width": 252,
                    "height": 189
                },
                {
                    "width": 504,
                    "height": 378
                },
                {
                    "width": 1008,
                    "height": 756
                },
                {
                    "width": 2016,
                    "height": 1512
                },
                {
                    "width": 4032,
                    "height": 3024
                }
            ]
        }

        thumbnail = self.manifest.create_thumbnail_from_iiif(image_info_url)[0]

        # check thumbnail matches preferred size
        self.assertEqual(thumbnail.height, 378)
        self.assertEqual(thumbnail.width, 504)

        # check thumbnail id
        self.assertEqual(thumbnail.id, "https://fixtures.iiif.io/other/level0/Glen/photos/gottingen/full/504,378/0/default.jpg")

        # check thumbnail service
        self.assertEqual(thumbnail.service[0].profile, "level0")
        self.assertEqual(thumbnail.service[0].type, "ImageService3")
