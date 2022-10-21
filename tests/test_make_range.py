import unittest

from iiif_prezi3 import Manifest, Range


class MakeRangeTest(unittest.TestCase):
    def setUp(self):
        self.manifest = Manifest(label="manifest")

    def test_add_range(self):
        r = self.manifest.make_range()
        assert isinstance(self.manifest.structures, list)
        assert isinstance(self.manifest.structures[-1], Range)
        assert isinstance(r, Range)
