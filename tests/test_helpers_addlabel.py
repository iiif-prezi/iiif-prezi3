import unittest

from iiif_prezi3 import Annotation, Canvas, config


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

    def test_annotation(self):
        """Test that label is added via add_label to an annotation."""
        default = config.configs['helpers.auto_fields.AutoLang'].auto_lang

        a = Annotation()

        # First test annotation has a label field
        a.label = {"en": ["test label"]}
        self.assertEqual(a.label, {"en": ["test label"]})

        # then check if you can use the label
        a = Annotation()
        a.add_label("test")
        self.assertEqual(a.label, {default: ["test"]})
