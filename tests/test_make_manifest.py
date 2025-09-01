import unittest

from iiif_prezi3 import Collection, Homepage, Reference, config


class MakeManifestTest(unittest.TestCase):

    def setUp(self):
        self.collection = Collection()

    def test_make_manifest(self):
        config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
        homepage = Homepage(
            id="https://www.getty.edu/art/collection/object/103RQQ",
            type="Text",
            label="Home page at the Getty Museum Collection",
            format="text/html",
            language=["en"]
        )
        manifest = self.collection.make_manifest(
            id='http://example.org/iiif/1',
            label='default label',
            homepage=homepage,
        )
        self.assertEqual(len(self.collection.items), 1)
        self.assertIsInstance(self.collection.items[0], Reference)
        self.assertEqual(manifest.label,
                         {'en': ['default label']})

        self.assertEqual(manifest.homepage[0], homepage)
