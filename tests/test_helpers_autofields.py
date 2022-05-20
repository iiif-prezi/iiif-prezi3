import unittest

from iiif_prezi3 import Manifest, config


class CanvasHelpersTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_lang_constructor(self):
        """Test that label is manipulated during object construction."""
        m = Manifest(label="string")
        self.assertEqual(m.label, str({"none": ["string"]}))
        m = Manifest(label=["string", "string2"])
        self.assertEqual(m.label, str({"none": ["string", "string2"]}))

    def test_lang_setattr(self):
        """Test that label is manipulated during property setting."""
        m = Manifest(label="string")
        m.label = "another string"
        self.assertEqual(m.label, str({"none": ["another string"]}))
        m.label = ["string3", "string4"]
        self.assertEqual(m.label, str({"none": ["string3", "string4"]}))

    def test_id_constructor(self):
        """Test that id is added during object construction."""
        m = Manifest(label="a")
        self.assertEqual(m.id, 'http://example.org/iiif/1')

    def test_lang_config(self):
        """Test that lang config is respected."""
        curr = config.configs['helpers.auto_fields.AutoLang'].auto_lang
        config.configs['helpers.auto_fields.AutoLang'].auto_lang = "de"
        m = Manifest(label="german")
        self.assertEqual(m.label, str({"de": ["german"]}))
        config.configs['helpers.auto_fields.AutoLang'].auto_lang = curr

    def test_id_config(self):
        """Test that id config is respected."""
        curr = config.configs['helpers.auto_fields.AutoId'].auto_type
        config.configs['helpers.auto_fields.AutoId'].auto_type = "uuid"
        m = Manifest(label="string")
        self.assertEqual(len(m.id), 60)
        config.configs['helpers.auto_fields.AutoId'].auto_type = curr
