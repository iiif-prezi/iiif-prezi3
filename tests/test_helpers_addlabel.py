import unittest

from iiif_prezi3 import Canvas, config


class AddLabelHelperTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_add_label(self):
        """Test that label is added via add_label."""
        default = config.configs['helpers.auto_fields.AutoLang'].auto_lang

        c = Canvas()
        self.assertEqual(c.label, None)
        c.add_label("test")
        self.assertEqual(c.label, {default: ["test"]})
        c.add_label("test2")
        self.assertEqual(c.label, {default: ["test", "test2"]})
        c.add_label("test", "en")
        self.assertEqual(c.label, {default: ["test", "test2"], "en": ["test"]})
        c.add_label("test2", "en")
        self.assertEqual(c.label, {default: ["test", "test2"], "en": ["test", "test2"]})
