import sys
import unittest

from pydantic import ValidationError

from iiif_prezi3 import Canvas

sys.path.insert(1, '.')


class Set_hwd(unittest.TestCase):

    def setUp(self):
        canvasid = 'http://iiif.example.org/prezi/CanvasID/01'
        acanvas = Canvas(id=canvasid, type='Canvas', label={'en': ['default lab']})
        self.acanvas = acanvas

    def test_assignment(self):
        """Test if the assignment of height, width, and duration works."""
        height = 100
        width = 200
        duration = 300.23
        self.acanvas.set_hwd(height=height, width=width, duration=duration)
        self.assertEqual(height, self.acanvas.height)
        self.assertEqual(width, self.acanvas.width)
        self.assertEqual(duration, self.acanvas.duration)

    def test_arguments_combination(self):
        """If a Canvas has either of height and width, it must have the other."""
        height = '100'
        width = '200'
        duration = '300.23'
        with self.assertRaises(TypeError):
            self.acanvas.set_hwd(height=height, width=None, duration=duration)
        with self.assertRaises(TypeError):
            self.acanvas.set_hwd(height=None, width=width, duration=duration)
        with self.assertRaises(TypeError):
            self.acanvas.set_hwd(height=None, width=None, duration=None)

    def test_pydantic_validation(self):
        """Test if pydantic validate the assignment of height, width, and duration."""
        height = 'test'
        width = 'test'
        duration = 'test'
        with self.assertRaises(ValidationError):
            self.acanvas.set_hwd(height=height, width=134, duration=None)
        with self.assertRaises(ValidationError):
            self.acanvas.set_hwd(height=123, width=width, duration=None)
        with self.assertRaises(ValidationError):
            self.acanvas.set_hwd(height=None, width=None, duration=duration)
