import sys
sys.path.insert(1,'.')
import json
import unittest

from iiif_prezi3 import Manifest, Canvas
from iiif_prezi3.helpers import canvas_sizes,ident


class BasicTest(unittest.TestCase):

    def testLoadManifest(self):
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

    def testNewManifest(self):
        manifest = Manifest(id='http://iiif.example.org/prezi/Manifest/0', type='Manifest', label={'en': 'default label'})
        #manifest.id = 'http://iiif.example.org/prezi/Manifest/0'
        #manifest.label = {'en': 'default label'}

        canvas = Canvas(id='http://iiif.example.org/prezi/Canvas/0')
        canvas.height = 100
        canvas.width = 200

        canvas2 = Canvas(id='http://iiif.example.org/prezi/Canvas/1')
        canvas2.height = 100

        manifest.items = [canvas, canvas2]

        data =  json.loads(manifest.json(exclude_unset=True))
        print (json.dumps(data, indent=4))
        print ('id: {}'.format(type(manifest.id)))
        print ('id as string: {}'.format(str(manifest.id)))
        print ('id prop: {}'.format(manifest.id))
        print ('Label: {}'.format(manifest.label))
        print ('Type: {}'.format(manifest.type))
        self.assertEqual("Unexpected Manifest id ", manifest.id, 'http://iiif.example.org/prezi/Manifest/0')
        self.assertEqual("Unexpected Canvas id", canvas.id, 'http://iiif.example.org/prezi/Canvas/1')


        self.assertEqual("Unexpected Manifest id in json", data["id"], 'http://iiif.example.org/prezi/Manifest/0')
        self.assertEqual("Unexpected Canvas id", data["items"][0]["id"], 'http://iiif.example.org/prezi/Canvas/1')
        
    def testOverloadCanvas(self):
        manifest = Manifest(id='http://iiif.example.org/prezi/Manifest/0', type='Manifest', label={'en': 'default label'})

        canvas = Canvas(id='http://iiif.example.org/prezi/Canvas/1',label={'en': "test"})
        canvas.height = 100
        canvas.width = 200
        manifest.items = [ canvas ] 
        #print ('Canvas id {}'.format(canvas.id))

        self.assertEqual(manifest.widest_canvas(), "Maximum canvas width: 200")


if __name__ == '__main__':
    unittest.main()
