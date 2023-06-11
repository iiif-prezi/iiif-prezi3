import json
import sys
import unittest

from pydantic import ValidationError

from iiif_prezi3 import Canvas, Manifest

sys.path.insert(1, '.')


class BasicTest(unittest.TestCase):

    def test_copy_on_model_validation(self):
        """Test if the copy_on_model_validation is working.

        Test if the user can change the values of the IIIF object after it has
        been instantiated using the reference to the original object.
        """
        originalID = 'http://iiif.example.org/TESTORIGINAL'
        amanifest = Manifest(id='http://iiif.example.org/prezi/Manifest/0', type='Manifest', label={'en': ['default label']})
        acanvas = Canvas(id='http://iiif.example.org/prezi/Manifest/0/canvas/01', type='Canvas', label={'en': ['default label']})
        asecondcanvas = Canvas(id=originalID, type='Canvas', label={'en': ['second label']})
        changedID = 'http://iiif.example.org/TESTCHANGED'
        amanifest.items = [acanvas, asecondcanvas]
        # we change the id of the first canvas
        acanvas.id = changedID
        self.assertEqual(amanifest.items[0].id, changedID)
        # we check that the second canvas has not been changed
        self.assertEqual(amanifest.items[1].id, originalID)

    def testLoadManifest(self):
        """Tests JSON file opening, extension is picked up, and the fields are correct."""
        with open('tests/fixtures/0003-mvm-video.json') as json_file:
            data = json.load(json_file)

            m = Manifest(**data)

            # Manifest not over written so should still be the skeleton Manifest
            self.assertEqual(str(m.__class__), "<class 'iiif_prezi3.skeleton.Manifest'>")

            # Method from canvas_sizes.MaxHelper.widest_canvas should be avilable
            self.assertEqual(m.widest_canvas(), "Maximum canvas width: 640")

    def testNewManifest(self):
        """Testing if the creation of a Manifest in python carries through to the JSON output."""
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

        data = json.loads(manifest.json())

        self.assertEqual(manifest.id, 'http://iiif.example.org/prezi/Manifest/0', "Unexpected Manifest id ")
        self.assertEqual(canvas.id, 'http://iiif.example.org/prezi/Canvas/0', "Unexpected Canvas id")

        self.assertEqual(data["id"], 'http://iiif.example.org/prezi/Manifest/0', "Unexpected Manifest id in json")
        self.assertEqual('http://iiif.example.org/prezi/Canvas/0', data["items"][0]["id"], "Unexpected Canvas id", )

    def testReadAndSetId(self):
        """Test setting and changing the ID of a manifest including exception raised if set with an invalid value."""
        manifest = Manifest(id='http://iiif.example.org/prezi/Manifest/0', type='Manifest', label={'en': ['label']})
        self.assertEqual(manifest.id, 'http://iiif.example.org/prezi/Manifest/0', "Unexpected Manifest id ")

        manifest.id = 'http://iiif.example.org/prezi/Manifest/new'

        self.assertEqual(manifest.id, 'http://iiif.example.org/prezi/Manifest/new', "Expected manifest id to change")

        # invalid id:
        with self.assertRaises(ValidationError):
            manifest.id = 'invalid_id'

    def testLabel(self):
        """Test setting up a label."""
        manifest = Manifest(id='http://iiif.example.org/prezi/Manifest/0', type='Manifest', label={'en': ['default label']})

        self.assertTrue('en' in manifest.label, 'Manifest seems to be missing English label')
        self.assertEqual(manifest.label['en'][0], 'default label', 'Unexpected label for manifest')

    def test_context_default(self):
        """Test that @context is included by default for .json() calls."""
        manifest = Manifest(id='http://iiif.example.org/prezi/Manifest/0', type='Manifest', label={'en': ['default label']})
        manifest_json = manifest.json()

        self.assertEqual(manifest_json[:61], '{"@context": "http://iiif.io/api/presentation/3/context.json"')

    def test_context_jsonld(self):
        """Test that @context is included by default for .jsonld() calls."""
        manifest = Manifest(id='http://iiif.example.org/prezi/Manifest/0', type='Manifest', label={'en': ['default label']})
        manifest_json = manifest.jsonld()

        self.assertEqual(manifest_json[:61], '{"@context": "http://iiif.io/api/presentation/3/context.json"')

    def test_context_excluded(self):
        """Test that @context is excluded when requested."""
        manifest = Manifest(id='http://iiif.example.org/prezi/Manifest/0', type='Manifest', label={'en': ['default label']})
        manifest_json = manifest.json(exclude_context=True)

        self.assertEqual(manifest_json[:49], '{"id": "http://iiif.example.org/prezi/Manifest/0"')

    def text_jsonld_context_excluded(self):
        """Test that @context is not excluded from .jsonld() calls, even when requested."""
        manifest = Manifest(id='http://iiif.example.org/prezi/Manifest/0', type='Manifest', label={'en': ['default label']})
        manifest_json = manifest.jsonld(exclude_context=True)

        self.assertEqual(manifest_json[:61], '{"@context": "http://iiif.io/api/presentation/3/context.json"')


if __name__ == '__main__':
    unittest.main()
