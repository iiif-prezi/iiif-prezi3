import unittest

from iiif_prezi3 import Collection


class MakeCollectionTest(unittest.TestCase):

    def setUp(self):
        self.parent_collection = Collection()

    def test_make_collection(self):
        child_collection = self.parent_collection.make_collection(
            id='http://iiif.example.org/prezi/Manifest/0',
            label="Example Collection"
        )
        self.assertEqual(len(self.parent_collection.items), 1)
        self.assertEqual(child_collection.id,
                         'http://iiif.example.org/prezi/Manifest/0')

    def test_make_collection_ref(self):
        child_collection = self.parent_collection.make_collection_ref(
            id='http://iiif.example.org/prezi/Collection/0',
            label="Example CollectionRef"
        )
        self.assertEqual(len(self.parent_collection.items), 1)
        self.assertFalse(hasattr(child_collection, 'items'))
