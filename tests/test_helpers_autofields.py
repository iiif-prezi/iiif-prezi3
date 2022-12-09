import unittest

from iiif_prezi3 import Collection, Manifest, config


class AutoFieldsHelpersTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_lang_constructor(self):
        """Test that label is manipulated during object construction."""
        m = Manifest(label="string")
        self.assertEqual(m.label, {"none": ["string"]})
        m = Manifest(label=["string", "string2"])
        self.assertEqual(m.label, {"none": ["string", "string2"]})

    def test_lang_setattr(self):
        """Test that label is manipulated during property setting."""
        m = Manifest(label="string")
        m.label = "another string"
        self.assertEqual(m.label, {"none": ["another string"]})
        m.label = ["string3", "string4"]
        self.assertEqual(m.label, {"none": ["string3", "string4"]})

    def test_id_constructor(self):
        """Test that id is added during object construction."""
        m = Manifest(label="a")
        self.assertTrue(m.id.startswith('http://example.org/iiif/'))

    def test_lang_config(self):
        """Test that lang config is respected."""
        curr = config.configs['helpers.auto_fields.AutoLang'].auto_lang
        config.configs['helpers.auto_fields.AutoLang'].auto_lang = "de"
        m = Manifest(label="german")
        self.assertEqual(m.label, {"de": ["german"]})
        config.configs['helpers.auto_fields.AutoLang'].auto_lang = curr

    def test_id_config(self):
        """Test that id config is respected."""
        curr = config.configs['helpers.auto_fields.AutoId'].auto_type
        config.configs['helpers.auto_fields.AutoId'].auto_type = "uuid"
        m = Manifest(label="string")
        self.assertEqual(len(m.id), 60)
        config.configs['helpers.auto_fields.AutoId'].auto_type = curr

    def test_int_per_type(self):
        """Test that the int-per-type helper works."""
        curr = config.configs['helpers.auto_fields.AutoId'].auto_type
        config.configs['helpers.auto_fields.AutoId'].auto_type = "int-per-type"
        m = Manifest(label="autoint")
        self.assertEqual('http://example.org/iiif/Manifest/0', m.id)
        m2 = Manifest(label="autoint2")
        self.assertEqual('http://example.org/iiif/Manifest/1', m2.id)
        c = Collection()
        self.assertEqual('http://example.org/iiif/Collection/0', c.id)
        config.configs['helpers.auto_fields.AutoId'].auto_type = curr

    def test_custom_slug(self):
        """Test that setting a custom slug for a specific type works."""
        curr_type = config.configs['helpers.auto_fields.AutoId'].auto_type
        config.configs['helpers.auto_fields.AutoId'].auto_type = "int-per-type"
        config.configs['helpers.auto_fields.AutoId'].translation["Manifest"] = "mani"
        m = Manifest(label="custom slug")
        self.assertEqual('http://example.org/iiif/mani/0', m.id)
        config.configs['helpers.auto_fields.AutoId'].auto_type = curr_type
        del (config.configs['helpers.auto_fields.AutoId'].translation["Manifest"])
