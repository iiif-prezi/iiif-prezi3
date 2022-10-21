import unittest

from iiif_prezi3 import Manifest, Canvas

class MakeManifestTest(unittest.TestCase):

    def setUp(self):
        self.manifest = Manifest()

    def test_make_manifest(self):
        canvas = self.manifest.make_canvas(
            label={'en': ['Canvas label']})
        self.assertEqual(len(self.manifest.items), 1)
        self.assertIsInstance(self.manifest.items[0], Canvas)
        self.assertEqual(canvas.label,
                         {'en': ['Canvas label']})
