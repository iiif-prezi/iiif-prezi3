import unittest

from iiif_prezi3 import (AccompanyingCanvas, Canvas, Collection,
                         LinkedResource, Manifest, PlaceholderCanvas, Provider)


class AddSeeAlsoTest(unittest.TestCase):

    def setUp(self):
        self.base = "https://example.org/iiif"
        self.linked_resource = LinkedResource(
            id=f"{self.base}/metadata/1",
            type="Dataset",
            label={"en": ["Item Metadata"]},
            format="application/json"
        )
        self.other_linked_resource = LinkedResource(
            id=f"{self.base}/metadata/2",
            type="Dataset",
            label={"en": ["Other Metadata"]},
            format="application/json"
        )
        self.collection = Collection(label="test label")
        self.manifest = Manifest(label="test label")
        self.canvas = Canvas(id=f"{self.base}/canvas/1")
        self.ac_canvas = AccompanyingCanvas(id=f"{self.base}/canvas/2", type="Canvas")
        self.ph_canvas = PlaceholderCanvas(id=f"{self.base}/canvas/3", type="Canvas")
        self.provider = Provider(id=f"{self.base}/provider/1", label="test provider")

    def test_add_see_also_to_collection(self):
        self.collection.add_see_also(self.linked_resource)
        self.assertEqual(self.collection.seeAlso.root, [self.linked_resource])

    def test_add_see_also_to_manifest(self):
        self.manifest.add_see_also(self.linked_resource)
        self.assertEqual(self.manifest.seeAlso.root, [self.linked_resource])

    def test_add_see_also_to_canvas(self):
        self.canvas.add_see_also(self.linked_resource)
        self.assertEqual(self.canvas.seeAlso.root, [self.linked_resource])

    def test_add_see_also_to_accompanying_canvas(self):
        self.ac_canvas.add_see_also(self.linked_resource)
        self.assertEqual(self.ac_canvas.seeAlso.root, [self.linked_resource])

    def test_add_see_also_to_placeholder_canvas(self):
        self.ph_canvas.add_see_also(self.linked_resource)
        self.assertEqual(self.ph_canvas.seeAlso.root, [self.linked_resource])

    def test_add_see_also_to_provider(self):
        self.provider.add_see_also(self.linked_resource)
        self.assertEqual(self.provider.seeAlso.root, [self.linked_resource])

    def test_add_multiple_see_also(self):
        self.manifest.add_see_also(self.linked_resource)
        self.manifest.add_see_also(self.other_linked_resource)
        self.assertEqual(
            self.manifest.seeAlso.root,
            [self.linked_resource, self.other_linked_resource]
        )

    def test_add_see_also_preserves_existing_entries_set_directly(self):
        self.manifest.seeAlso = [self.linked_resource]
        self.manifest.add_see_also(self.other_linked_resource)
        self.assertEqual(
            self.manifest.seeAlso.root,
            [self.linked_resource, self.other_linked_resource]
        )

    def test_add_invalid_instance_to_see_also(self):
        with self.assertRaises(TypeError):
            self.manifest.add_see_also(self.collection)


if __name__ == '__main__':
    unittest.main()
