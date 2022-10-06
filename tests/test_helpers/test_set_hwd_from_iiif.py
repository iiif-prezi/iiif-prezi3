import unittest
from unittest.mock import Mock, patch

import requests

from iiif_prezi3 import Canvas


class SetHwdFromIIIFTests(unittest.TestCase):

    def setUp(self):
        self.canvas = Canvas(id='http://iiif.example.org/prezi/Canvas/0')

    @patch('iiif_prezi3.helpers.set_hwd_from_iiif.requests.get')
    def test_set_hwd_from_iiif(self, mockrequest_get):
        image_id = 'http://iiif.example.org/images/1234abcd'
        image_info_url = f'{image_id}/info.json'
        # image api url without info.json
        self.canvas.set_hwd_from_iiif(image_id)
        mockrequest_get.assert_called_with(image_info_url)

        # image api url with info.json
        mockrequest_get.reset_mock()
        self.canvas.set_hwd_from_iiif(image_id)
        mockrequest_get.assert_called_with(image_info_url)

        # image url with trailing slash
        mockrequest_get.reset_mock()
        self.canvas.set_hwd_from_iiif(image_id + "/")
        mockrequest_get.assert_called_with(image_info_url)

        # non-200 response
        mockresponse = Mock(status_code=404)
        # This is necessary otherwise the mocked response correctly calls raise_for_status, but doesn't terminate the
        # code flow like it would in normal usage (because there's not actually an exception) so it would try and call
        # set_hwd with non-existent values and error out incorrectly.
        mockresponse.raise_for_status.side_effect = requests.exceptions.HTTPError
        mockrequest_get.return_value = mockresponse
        with self.assertRaises(requests.exceptions.HTTPError):
            self.canvas.set_hwd_from_iiif(image_id)
            # non-200 should raise exception for status
            mockresponse.raise_for_status.assert_called_once()

        # 200 response but not valid json should raise exception
        mockresponse.status_code = 200
        mockresponse.json.side_effect = requests.exceptions.JSONDecodeError("", "", 0)  # JSONDecodeError needs arguments
        with self.assertRaises(requests.exceptions.JSONDecodeError):
            self.canvas.set_hwd_from_iiif(image_id)

        # successful response with dimensions
        mockresponse.json.side_effect = None
        # set mock to return minimal image api response
        mockresponse.json.return_value = {
            "@context": "http://iiif.io/api/image/2/context.json",
            "@id": image_id,
            "protocol": "http://iiif.io/api/image",
            "width": 4821,
            "height": 6608
        }
        # patch the method this helper calls so we can inspect
        with patch.object(Canvas, 'set_hwd') as mock_set_hwd:
            self.canvas.set_hwd_from_iiif(image_id)
            mock_set_hwd.assert_called_with(6608, 4821)
