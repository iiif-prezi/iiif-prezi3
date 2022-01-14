import sys
sys.path.insert(1,'.')
import json
import unittest
from pydantic import ValidationError

from iiif_prezi3 import Manifest, Canvas
from iiif_prezi3.helpers import canvas_sizes


class BasicTest(unittest.TestCase):

    def testLoadManifest(self):
        '''
            Test the opening of a JSON file
            and checking the extension is picked up and
            the fields are correct
        '''
        with open('tests/fixtures/0003-mvm-video.json') as json_file:
            data = json.load(json_file)

            m = Manifest(**data)
            c = m.items[0]

            # Manifest not over written so should still be the skeleton Manifest
            self.assertEqual(str(m.__class__), "<class 'iiif_prezi3.skeleton.Manifest'>")

            # Method from canvas_sizes.MaxHelper.widest_canvas should be avilable 
            self.assertEqual(m.widest_canvas(), "Maximum canvas width: 640")

    def testNewManifest(self):
        '''
            Testing if the creation of a Manifest in python carries through to the JSON output
        '''
        manifest = Manifest(id='http://iiif.example.org/prezi/Manifest/0', type='Manifest', label={'en': ['default label']})
        
        canvas = Canvas(id='http://iiif.example.org/prezi/Canvas/0')
        canvas.height = 100
        canvas.width = 200

        canvas2 = Canvas(id='http://iiif.example.org/prezi/Canvas/1')
        canvas2.height = 100
        canvas2.width = 100

        manifest.items = [canvas, canvas2]

        # test manifest has the helper method
        self.assertEqual(manifest.widest_canvas(), "Maximum canvas width: 200")

        data =  json.loads(manifest.json(exclude_unset=True))
        
        self.assertEqual(manifest.id, 'http://iiif.example.org/prezi/Manifest/0', "Unexpected Manifest id ")
        self.assertEqual(canvas.id, 'http://iiif.example.org/prezi/Canvas/0', "Unexpected Canvas id")

        self.assertEqual(data["id"], 'http://iiif.example.org/prezi/Manifest/0', "Unexpected Manifest id in json")
        self.assertEqual('http://iiif.example.org/prezi/Canvas/0', data["items"][0]["id"],  "Unexpected Canvas id", )
        

    def testReadAndSetId(self):
        '''
            Test setting and changing the ID of 
            a manifest including exception raised if 
            set with an invalid value.
        '''
        manifest = Manifest(id='http://iiif.example.org/prezi/Manifest/0', type='Manifest', label={'en': 'label'})
        self.assertEqual(manifest.id, 'http://iiif.example.org/prezi/Manifest/0', "Unexpected Manifest id ")

        manifest.id = 'http://iiif.example.org/prezi/Manifest/new'

        self.assertEqual(manifest.id, 'http://iiif.example.org/prezi/Manifest/new', "Expected manifest id to change")

        # invalid id:
        with self.assertRaises(ValidationError):
            manifest.id = 'invalid_id'

    def testLabel(self):
        manifest = Manifest(id='http://iiif.example.org/prezi/Manifest/0', type='Manifest', label={'en': 'default label'})
        print ('Label: {}'.format(manifest.label))

if __name__ == '__main__':
    unittest.main()
