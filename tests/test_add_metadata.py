import unittest

from iiif_prezi3 import Collection, LngString


class AddMetadataTest(unittest.TestCase):
    def setUp(self):
        self.collection = Collection()

    def test_add_metadata_string(self):
        self.collection.add_metadata("label", "value")
        assert isinstance(self.collection.metadata, list)
        assert self.collection.metadata[-1].label == {'none': ['label']}
        assert self.collection.metadata[-1].value == {'none': ['value']}

    def test_add_metadata_dict(self):
        label = {"en": ["label"]}
        value = {"en": ["value"]}
        self.collection.add_metadata(label, value)
        assert isinstance(self.collection.metadata, list)
        assert self.collection.metadata[-1].label == {'en': ['label']}
        assert self.collection.metadata[-1].value == {'en': ['value']}

    def test_add_metadata_lngstring(self):
        label = LngString(__root__={'en': ['label']})
        value = LngString(__root__={'en': ['value']})
        self.collection.add_metadata(label, value)
        assert isinstance(self.collection.metadata, list)
        assert self.collection.metadata[-1].label == {'en': ['label']}
        assert self.collection.metadata[-1].value == {'en': ['value']}

    def test_validate_different_argtypes(self):
        label = "label"
        value = 5
        self.assertRaises(TypeError, self.collection.add_metadata, label, value)

    def test_invalid_argtypes(self):
        label = ["label"]
        value = ["value"]
        self.assertRaises(TypeError, self.collection.add_metadata, label, value)
