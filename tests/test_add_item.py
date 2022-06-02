import unittest

from pydantic import ValidationError

from iiif_prezi3 import (Annotation, AnnotationPage, Canvas, Collection,
                         Manifest, Reference, ResourceItem)


class AddItemTests(unittest.TestCase):

    def setUp(self):
        self.c = Collection(label="collection")
        self.m = Manifest(label="manifest")
        self.ca = Canvas(label="first canvas")
        self.ca2 = Canvas(label="second canvas")
        self.ap = AnnotationPage()
        self.a = Annotation(target=self.c.id)

    def test_add_item(self):
        """Test that a Canvas added to an empty Manifest creates and populates items."""
        self.m.add_item(self.ca)
        self.assertEqual(len(self.m.items), 1)
        self.assertEqual(self.m.items[0], self.ca)

    def test_add_item_existing(self):
        """Test that a Canvas is added correctly to a Manifest with existing items."""
        self.m.items = [self.ca]
        self.m.add_item(self.ca2)
        self.assertEqual(len(self.m.items), 2)
        self.assertEqual(self.m.items[0], self.ca)
        self.assertEqual(self.m.items[1], self.ca2)

    def test_add_manifest_to_collection(self):
        """Test that a Manifest added to a collection is done so by Reference."""
        self.c.add_item(self.m)
        self.assertIsInstance(self.c.items[0], Reference)

    def test_add_by_reference(self):
        """Test that an item can be added by Reference."""
        self.ap.add_item(self.a)
        self.assertEqual(len(self.ap.items), 1)
        self.c.add_item_by_reference(self.ap)
        self.assertNotEqual(self.c.items[0], self.ap)
        self.assertIsInstance(self.c.items[0], Reference)
        self.assertEqual(self.c.items[0].id, self.ap.id)

    def test_add_by_reference_with_thumbnail(self):
        """Test that an item added by Reference preserves the thumbnail where appropriate."""
        self.m.thumbnail = [ResourceItem(id="https://example.org/img/thumb.jpg", type="Image", format="image/jpeg", width=300, height=300)]
        self.c.add_item_by_reference(self.m)
        self.assertIsInstance(self.c.items[0], Reference)
        self.assertEqual(self.c.items[0].thumbnail, self.m.thumbnail)

    def test_add_invalid_single(self):
        """Test that adding an invalid item fails when the acceptable items can only be one type (e.g a Collection to a Canvas)."""
        with self.assertRaises(ValidationError):
            self.ca.add_item(self.c)

    # TODO: Re-enable this test once we fix the reference issue in the schema + skeleton
    # def test_add_invalid_coercion(self):
    #     """Test that adding an invalid item fails when the acceptable items can be several classes (e.g a Canvas to a Collection)."""
    #     with self.assertRaises(ValidationError):
    #         self.c.add_item(self.c)
