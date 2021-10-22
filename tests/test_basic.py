import sys
sys.path.insert(1,'.')
import json
import unittest

from iiif_prezi3 import Manifest, Canvas
from iiif_prezi3.helpers import canvas_sizes


class BasicTest(unittest.TestCase):

    def test_manifest(self):
        with open('tests/fixtures/0003-mvm-video.json') as json_file:
            data = json.load(json_file)

            m = Manifest(**data)
            c = m.items[0]
            print("Canvas instantiated as part of a manifest")
            print("-----")
            print("Manifest class:", m.__class__)
            print("Manifest helper:", m.widest_canvas())
            print("Canvas class:", c.__class__)
            self.assertEqual(m.widest_canvas(), "Maximum canvas width: 640")

if __name__ == '__main__':
    unittest.main()
