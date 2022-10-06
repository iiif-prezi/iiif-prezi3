import unittest

from iiif_prezi3 import Manifest, Range


class AddRangeTest(unittest.TestCase):
    def setUp(self):
        self.manifest = Manifest(label="manifest")
        self.range = Range(type="Range")

    def test_add_range(self):
        self.manifest.add_range(self.range)
        assert isinstance(self.manifest.structures, list)
        assert self.manifest.structures[-1] == self.range
