import unittest

from iiif_prezi3 import Collection, Reference


class MakeManifestTest(unittest.TestCase):

    def setUp(self):
        self.collection = Collection()

    def test_make_manifest(self):
        manifest = self.collection.make_manifest(
            label={'en': ['default label']})
        self.assertEqual(len(self.collection.items), 1)
        self.assertIsInstance(self.collection.items[0], Reference)
        self.assertEqual(manifest.label,
                         {'en': ['default label']})
