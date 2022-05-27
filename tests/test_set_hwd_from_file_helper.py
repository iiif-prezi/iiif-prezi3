import unittest

from iiif_prezi3 import Canvas


class SetHeightWidthDurationFileHelperTests(unittest.TestCase):
    def setUp(self):
        self.canvas = Canvas(id="http://iiif.example.org/prezi/Canvas/0")
        self.test_image = "tests/fixtures/resources/page1-full.png"

    def test_set_hwd_from_filepath_notimage(self):
        self.assertRaises(NotImplementedError, self.canvas.set_hwd_from_file, "foo.mp3")

    def test_set_hwd_from_filepath(self):
        self.canvas.set_hwd_from_file(self.test_image)
        self.assertEqual(self.canvas.width, 1200)  # width
        self.assertEqual(self.canvas.height, 1800)  # height
        self.assertEqual(self.canvas.duration, None)  # duration

    def test_set_hwd_from_fileobject(self):
        with open(self.test_image, "rb") as image_file:
            self.canvas.set_hwd_from_file(image_file)
        self.assertEqual(self.canvas.width, 1200)  # width
        self.assertEqual(self.canvas.height, 1800)  # height
        self.assertEqual(self.canvas.duration, None)  # duration
