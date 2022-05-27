import unittest

from iiif_prezi3 import Canvas, Collection, LngString, Manifest, Range


class AddMetadataTest(unittest.TestCase):
    def setUp(self):
        self.collection = Collection()

    def test_add_metadata(self):
        self.collection.add_metadata("label", "value")
        assert isinstance(self.collection.metadata, list)
        assert self.collection.metadata[-1].label == {'none': ['label']}
        assert self.collection.metadata[-1].value == {'none': ['value']}
