import sys
sys.path.insert(1,'.')
import json
import unittest

from iiif_prezi3.prezi3 import Manifest, Canvas 


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
            print("Canvas helper:", c.helper_function())

if __name__ == '__main__':
    unittest.main()
