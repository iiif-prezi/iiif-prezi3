import unittest

from iiif_prezi3 import Canvas, Manifest


class MakeManifestTest(unittest.TestCase):

    def setUp(self):
        self.manifest = Manifest(label={'en': ['Manifest label']})

    def test_make_canvas(self):
        canvas = self.manifest.make_canvas(
            label={'en': ['Canvas label']})
        self.assertEqual(len(self.manifest.items), 1)
        self.assertIsInstance(self.manifest.items[0], Canvas)
        self.assertEqual(canvas.label,
                         {'en': ['Canvas label']})
