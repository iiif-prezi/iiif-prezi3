import unittest

from pydantic import ValidationError

from iiif_prezi3 import Canvas


class CanvasValidatorsTests(unittest.TestCase):
    def test_hw_andor_d(self):
        """Test the height&width and/or duration validator."""
        with self.assertRaises(ValidationError):
            Canvas()
        c = Canvas(height=100, width=100)
        self.assertEqual(c.height, 100)
        c = Canvas(duration=100.0)
        self.assertEqual(c.duration, 100.0)

    def test_h_and_w(self):
        """Test that including height or width requires the other."""
        with self.assertRaises(ValidationError):
            Canvas(height=100)
        with self.assertRaises(ValidationError):
            Canvas(width=100)
        with self.assertRaises(ValidationError):
            Canvas(height=100, duration=100.0)
