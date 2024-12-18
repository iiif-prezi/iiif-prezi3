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
        self.assertEqual(thumbnail.height, 189)
        self.assertEqual(thumbnail.width, 252)

        # check thumbnail id
        self.assertEqual(thumbnail.id, "https://fixtures.iiif.io/other/level0/Glen/photos/gottingen/full/252,189/0/default.jpg")

        # check thumbnail service
        self.assertEqual(thumbnail.service[0].profile, "level0")
        self.assertEqual(thumbnail.service[0].type, "ImageService3")

    @patch('iiif_prezi3.helpers.set_hwd_from_iiif.requests.get')
    def test_create_thumbnail_from_iiif_v2(self, mockrequest_get):
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
                    "formats": [
                        "jpg",
                        "png"
                    ],
                    "qualities": [
                        "default",
                        "color",
                        "gray"
                    ]
                }
            ],
            "protocol": "http://iiif.io/api/image",
            "tiles": [
                {
                    "height": 512,
                    "scaleFactors": [
                        1,
                        2,
                        4
                    ],
                    "width": 512
                }
            ],
            "width": 4032
        }

        thumbnail = self.manifest.create_thumbnail_from_iiif(image_info_url)[0]

        # check thumbnail matches preferred size
        self.assertEqual(thumbnail.height, 3024)
        self.assertEqual(thumbnail.width, 4032)

        # Since info_json has no sizes, use full/full
        self.assertEqual(thumbnail.id, "https://iiif.io/api/image/2.1/example/reference/918ecd18c2592080851777620de9bcb5-gottingen/full/full/0/default.jpg")

        # check thumbnail service
        self.assertEqual(thumbnail.service[0].profile, "http://iiif.io/api/image/2/level1.json")
        self.assertEqual(thumbnail.service[0].type, "ImageService2")

    @patch('iiif_prezi3.helpers.set_hwd_from_iiif.requests.get')
    def test_create_thumbnail_from_level_0_iiif_v3(self, mockrequest_get):
        image_id = 'https://iiif-test.github.io/test2/images/IMG_5949'
        image_info_url = f'{image_id}/info.json'
        mockresponse = Mock(status_code=200)
        mockrequest_get.return_value = mockresponse
        mockresponse.json.return_value = {
          "tiles": [
            {
              "scaleFactors": [
                32,
                16,
                8,
                4,
                2,
                1
              ],
              "width": 1024,
              "height": 1024
            }
          ],
          "protocol": "http://iiif.io/api/image",
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
          ],
          "profile": "level0",
          "width": 4032,
          "id": "https://iiif-test.github.io/test2/images/IMG_5949",
          "type": "ImageService3",
          "@context": "http://iiif.io/api/image/3/context.json",
          "height": 3024
        }

        thumbnail = self.manifest.create_thumbnail_from_iiif(image_info_url)[0]
        self.assertEqual(thumbnail.height, 189)
        self.assertEqual(thumbnail.width, 252)
        self.assertEqual(
            thumbnail.id,
    "https://iiif-test.github.io/test2/images/IMG_5949/full/252,189/0/default.jpg"
        )

        # check thumbnail service
        self.assertEqual(thumbnail.service[0].profile, "level0")
        self.assertEqual(thumbnail.service[0].type, "ImageService3")

    @patch('iiif_prezi3.helpers.set_hwd_from_iiif.requests.get')
    def test_create_thumbnail_from_level_0_iiif_v2(self, mockrequest_get):
        image_id = 'https://iiif-test.github.io/test2/images/IMG_8669'
        image_info_url = f'{image_id}/info.json'
        mockresponse = Mock(status_code=200)
        mockrequest_get.return_value = mockresponse
        mockresponse.json.return_value = {
          "tiles": [
            {
              "scaleFactors": [
                32,
                16,
                8,
                4,
                2,
                1
              ],
              "width": 1024,
              "height": 1024
            }
          ],
          "protocol": "http://iiif.io/api/image",
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
          ],
          "profile": "http://iiif.io/api/image/2/level0.json",
          "width": 4032,
          "@id": "https://iiif-test.github.io/test2/images/IMG_8669",
          "@context": "http://iiif.io/api/image/2/context.json",
          "height": 3024
        }

        thumbnail = self.manifest.create_thumbnail_from_iiif(image_info_url)[0]
        self.assertEqual(thumbnail.height, 189)
        self.assertEqual(thumbnail.width, 252)
        self.assertEqual(
            thumbnail.id,
            "https://iiif-test.github.io/test2/images/IMG_8669/full/252,/0/default.jpg"
        )
