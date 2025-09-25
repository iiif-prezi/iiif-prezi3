import unittest

from iiif_prezi3 import Collection, Manifest, config, Annotation, AccompanyingCanvas, AnnotationCollection, PlaceholderCanvas, Canvas, AnnotationBody, AnnotationPage

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

    def test_autolist_constructor(self):
        """Test that list properties are set correctly during construction."""
        m = Manifest(label="AutoList Test", behavior="paged")
        self.assertEqual(m.behavior, ["paged"])
        m2 = Manifest(label="AutoList Test", behavior=["continuous"])
        self.assertEqual(m2.behavior, ["continuous"])

    def test_autolist_setattr(self):
        """Test that list properties are set correctly during manipulation."""
        m = Manifest(label="AutoList Test", behavior="paged")
        self.assertEqual(m.behavior, ["paged"])
        m.behavior = "continuous"
        self.assertEqual(m.behavior, ["continuous"])

    def test_autolist_object_constructor(self):
        """Test that list properties are set during construction, when the list contains objects."""
        m = Manifest(label="AutoList Test", rendering={"type": "Text", "label": "Download OCR", "format": "text/plain"})
        self.assertIsInstance(m.rendering, list)
        self.assertEqual(m.rendering[0].format, "text/plain")
        m = Manifest(label="AutoList Test", rendering=[{"type": "Text", "label": "Download OCR", "format": "text/plain"}])
        self.assertIsInstance(m.rendering, list)
        self.assertEqual(m.rendering[0].format, "text/plain")

    def test_autolist_object_setattr(self):
        """Test that list properties are set correctly during manipulation, when the list contains objects."""
        m = Manifest(label="AutoList Test", rendering={"type": "Text", "label": "Download OCR", "format": "text/plain"})
        self.assertIsInstance(m.rendering, list)
        self.assertEqual(m.rendering[0].format, "text/plain")
        m.rendering = {"type": "Text", "label": "Download OCR", "format": "application/pdf"}
        self.assertIsInstance(m.rendering, list)
        self.assertEqual(m.rendering[0].format, "application/pdf")

    def test_autolist_nested_homepage(self):
        """Test that autolist properties are set correctly when the list is nested for homepage items."""
        m = Manifest(label="Nested Autolist Test", provider={"homepage": {"type": "Text", "format": "text/html", "language": "en"}})
        self.assertIsInstance(m.provider, list)
        self.assertIsInstance(m.provider[0].homepage, list)
        self.assertIsInstance(m.provider[0].homepage[0].language, list)

    def test_autolist_nested(self):
        """Test that autolist properties are set correctly when the list is nested."""
        m = Manifest(label="Nested Autolist Test", provider={"logo": {"id": "https://example.org/logo", "type": "Image", "format": "image/png", "service": {"type": "ImageService3", "profile": "level2"}}})
        self.assertIsInstance(m.provider, list)
        self.assertIsInstance(m.provider[0].logo, list)
        self.assertIsInstance(m.provider[0].logo[0].service, list)

    def _defaulter_in_object(self, cls, defaulter):
        for defaulter_class in cls._defaulters:
            if defaulter_class.__class__.__name__ == defaulter:
                return True
        return False    

    def test_auto_present(self):
        self.assertFalse(self._defaulter_in_object(Annotation, "AutoItems"), "Annotations should not have AutoItems")
        self.assertTrue(self._defaulter_in_object(Manifest, "AutoItems"), f"Expected Manifest to have AutoItems. It had: {Manifest._defaulters}")

        Manifest(label="string")

        self.assertTrue(self._defaulter_in_object(Manifest, "AutoItems"), f"Expected second call to create Manifest to also have AutoItems. It had: {Manifest._defaulters}")

        self.assertTrue(self._defaulter_in_object(AccompanyingCanvas, "AutoItems"), f"Expected AccompanyingCanvas to have AutoItems. It had: {AccompanyingCanvas._defaulters}")
        self.assertTrue(self._defaulter_in_object(PlaceholderCanvas, "AutoItems"), f"Expected PlaceholderCanvas to have AutoItems. It had: {PlaceholderCanvas._defaulters}")
        self.assertTrue(self._defaulter_in_object(AnnotationCollection, "AutoItems"), f"Expected AnnotationCollection to have AutoItems. It had: {AnnotationCollection._defaulters}")

    def test_canvas_annotations_auto_list(self):
        canvas = Canvas(label="test")

        body = AnnotationBody(id="http://example.com", type="Image")
        annotation = Annotation(motivation='painting', body=body, target=canvas.id)


        annotationPage = AnnotationPage()
        annotationPage.add_item(annotation)

        canvas.annotations = annotationPage 

        self.assertIsInstance(canvas.annotations, list, "Expected canvas.annotations to be a list")