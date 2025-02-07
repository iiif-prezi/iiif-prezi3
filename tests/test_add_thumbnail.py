import unittest
from unittest.mock import Mock, patch

from iiif_prezi3 import Manifest


class AddThumbnailTests(unittest.TestCase):

    def setUp(self):
        self.manifest = Manifest(label={'en': ['Manifest label']})

    @patch('iiif_prezi3.helpers.set_hwd_from_iiif.requests.get')
    def test_create_thumbnail_from_iiif_v3_sizes_not_level_0(self, mockrequest_get):
        # This fixture is hosted by UCLA but used in Recipe 0234-provider
        image_id = 'https://iiif.library.ucla.edu/iiif/3/UCLA-Library-Logo-double-line-2'
        image_info_url = f'{image_id}/info.json'

        # successful response with dimensions
        mockresponse = Mock(status_code=200)
        mockrequest_get.return_value = mockresponse
        # set mock to return minimal image api response
        mockresponse.json.return_value = {
          "@context": "http://iiif.io/api/image/3/context.json",
          "id": "https://iiif.library.ucla.edu/iiif/3/UCLA-Library-Logo-double-line-2",
          "type": "ImageService3",
          "protocol": "http://iiif.io/api/image",
          "profile": "level2",
          "width": 1200,
          "height": 502,
          "maxArea": 602400,
          "sizes": [
            {
              "width": 300,
              "height": 126
            },
            {
              "width": 600,
              "height": 251
            },
            {
              "width": 1200,
              "height": 502
            }
          ],
          "tiles": [
            {
              "width": 512,
              "height": 502,
              "scaleFactors": [
                1,
                2,
                4
              ]
            }
          ],
          "extraQualities": [
            "bitonal",
            "color",
            "gray"
          ],
          "extraFormats": [
            "tif",
            "gif"
          ],
          "extraFeatures": [
            "baseUriRedirect",
            "canonicalLinkHeader",
            "cors",
            "jsonldMediaType",
            "mirroring",
            "profileLinkHeader",
            "regionByPct",
            "regionByPx",
            "regionSquare",
            "rotationArbitrary",
            "rotationBy90s",
            "sizeByConfinedWh",
            "sizeByH",
            "sizeByPct",
            "sizeByW",
            "sizeByWh"
          ]
        }

        thumbnail = self.manifest.create_thumbnail_from_iiif(image_info_url)[0]

        # check thumbnail matches preferred size
        self.assertEqual(thumbnail.height, 251)
        self.assertEqual(thumbnail.width, 600)

        # check thumbnail id
        self.assertEqual(
            thumbnail.id,
            f"{image_id}/full/600,251/0/default.jpg"
        )

        # check thumbnail service
        self.assertEqual(thumbnail.service[0].profile, "level2")
        self.assertEqual(thumbnail.service[0].type, "ImageService3")

    @patch('iiif_prezi3.helpers.set_hwd_from_iiif.requests.get')
    def test_create_thumbnail_from_iiif_v2_sizes_not_level_0(self, mockrequest_get):
        # This fixture is hosted by UCLA but used in Recipe 0234-provider
        image_id = 'https://iiif.library.ucla.edu/iiif/2/UCLA-Library-Logo-double-line-2'
        image_info_url = f'{image_id}/info.json'

        # successful response with dimensions
        mockresponse = Mock(status_code=200)
        mockrequest_get.return_value = mockresponse
        # set mock to return minimal image api response
        mockresponse.json.return_value = {
            "@context": "http://iiif.io/api/image/3/context.json",
            "id": "https://iiif.library.ucla.edu/iiif/3/UCLA-Library-Logo-double-line-2",
            "type": "ImageService3",
            "protocol": "http://iiif.io/api/image",
            "profile": "level2",
            "width": 1200,
            "height": 502,
            "maxArea": 602400,
            "sizes": [
                {
                    "width": 300,
                    "height": 126
                },
                {
                    "width": 600,
                    "height": 251
                },
                {
                    "width": 1200,
                    "height": 502
                }
            ],
            "tiles": [
                {
                    "width": 512,
                    "height": 502,
                    "scaleFactors": [
                        1,
                        2,
                        4
                    ]
                }
            ],
            "extraQualities": [
                "bitonal",
                "color",
                "gray"
            ],
            "extraFormats": [
                "tif",
                "gif"
            ],
            "extraFeatures": [
                "baseUriRedirect",
                "canonicalLinkHeader",
                "cors",
                "jsonldMediaType",
                "mirroring",
                "profileLinkHeader",
                "regionByPct",
                "regionByPx",
                "regionSquare",
                "rotationArbitrary",
                "rotationBy90s",
                "sizeByConfinedWh",
                "sizeByH",
                "sizeByPct",
                "sizeByW",
                "sizeByWh"
            ]
        }

        thumbnail = self.manifest.create_thumbnail_from_iiif(image_info_url)[0]

        # check thumbnail matches preferred size
        self.assertEqual(thumbnail.height, 251)
        self.assertEqual(thumbnail.width, 600)

        # check thumbnail id
        self.assertEqual(
            thumbnail.id,
            f"{image_id}/full/600,251/0/default.jpg"
        )

        # check thumbnail service
        self.assertEqual(thumbnail.service[0].profile, "level2")
        self.assertEqual(thumbnail.service[0].type, "ImageService3")

    @patch('iiif_prezi3.helpers.set_hwd_from_iiif.requests.get')
    def test_create_thumbnail_from_iiif_v3_sizes_level0(self, mockrequest_get):
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
        self.assertEqual(
            thumbnail.id,
            f"{image_id}/full/504,378/0/default.jpg"
        )

        # check thumbnail service
        self.assertEqual(thumbnail.service[0].profile, "level0")
        self.assertEqual(thumbnail.service[0].type, "ImageService3")

    @patch('iiif_prezi3.helpers.set_hwd_from_iiif.requests.get')
    def test_create_thumbnail_from_level_0_iiif_v2_sizes_level0(self, mockrequest_get):
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
        self.assertEqual(thumbnail.height, 378)
        self.assertEqual(thumbnail.width, 504)
        self.assertEqual(
            thumbnail.id,
            "https://iiif-test.github.io/test2/images/IMG_8669/full/504,/0/default.jpg"
        )

    @patch('iiif_prezi3.helpers.set_hwd_from_iiif.requests.get')
    def test_v3_with_no_sizes_prop(self, mockrequest_get):
        image_id = 'https://iiif.io/api/image/3.0/example/reference/4ce82cef49fb16798f4c2440307c3d6f-newspaper-p1'
        image_info_url = f'{image_id}/info.json'
        mockresponse = Mock(status_code=200)
        mockrequest_get.return_value = mockresponse
        mockresponse.json.return_value = {
          "@context": "http://iiif.io/api/image/3/context.json",
          "extraFormats": [
            "jpg",
            "png"
          ],
          "extraQualities": [
            "default",
            "color",
            "gray"
          ],
          "height": 5000,
          "id": "https://iiif.io/api/image/3.0/example/reference/4ce82cef49fb16798f4c2440307c3d6f-newspaper-p1",
          "profile": "level1",
          "protocol": "http://iiif.io/api/image",
          "tiles": [
            {
              "height": 512,
              "scaleFactors": [
                1,
                2,
                4,
                8
              ],
              "width": 512
            }
          ],
          "type": "ImageService3",
          "width": 3602
        }

        thumbnail = self.manifest.create_thumbnail_from_iiif(image_info_url)[0]
        self.assertEqual(thumbnail.height, 694)
        self.assertEqual(thumbnail.width, 500)
        self.assertEqual(
            thumbnail.id,
            f"{image_id}/full/500,694/0/default.jpg"
        )

    @patch('iiif_prezi3.helpers.set_hwd_from_iiif.requests.get')
    def test_create_thumbnail_from_iiif_v2_no_sizes(self, mockrequest_get):
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
        self.assertEqual(thumbnail.height, 375)
        self.assertEqual(thumbnail.width, 500)

        # Since info_json has no sizes, use full/full
        self.assertEqual(thumbnail.id, "https://iiif.io/api/image/2.1/example/reference/918ecd18c2592080851777620de9bcb5-gottingen/full/500,/0/default.jpg")

        # check thumbnail service
        self.assertEqual(thumbnail.service[0].profile, "http://iiif.io/api/image/2/level1.json")
        self.assertEqual(thumbnail.service[0].type, "ImageService2")

    @patch('iiif_prezi3.helpers.set_hwd_from_iiif.requests.get')
    def test_create_thumbnail_from_iiif_giant_request_with_sizes(self, mockrequest_get):
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

        giant_thumbnail = self.manifest.create_thumbnail_from_iiif(image_info_url, preferred_width=7000)[0]
        self.assertEqual(giant_thumbnail.height, 3024)
        self.assertEqual(giant_thumbnail.width, 4032)
        self.assertEqual(
            giant_thumbnail.id,
            f"{image_id}/full/4032,/0/default.jpg"
        )
