import unittest

from iiif_prezi3 import AnnotationPage, Canvas, AnnotationBody


class CanvasHelpersTests(unittest.TestCase):
    def setUp(self):
        self.canvas = Canvas(id='http://iiif.example.org/prezi/Canvas/0')

    def test_add_image(self):
        anno_page = self.canvas.add_image(
            'http://iiif.example.org/prezi/Image/0',
            'http://iiif.example.org/prezi/Annotation/0',
            height=400)
        self.assertTrue(isinstance(anno_page, AnnotationPage), '`add_image` should return an AnnotationPage')
        self.assertEqual(len(self.canvas.items), 1)
        self.assertEqual(anno_page.items[0].id, 'http://iiif.example.org/prezi/Annotation/0')
        self.assertEqual(anno_page.items[0].target, 'http://iiif.example.org/prezi/Canvas/0')
        self.assertEqual(anno_page.items[0].dict()["body"]["id"], 'http://iiif.example.org/prezi/Image/0')
        self.assertEqual(anno_page.items[0].dict()["body"]["height"], 400)

    def test_add_thumbnail(self):
        canvas = self.canvas.add_thumbnail(
            'http://iiif.example.org/prezi/Image/0',
            height=200)
        self.assertTrue(isinstance(canvas, AnnotationBody), '`add_thumbnail` should return a AnnotationBody')
        self.assertEqual(len(self.canvas.thumbnail), 1)
        self.assertEqual(self.canvas.thumbnail[0].id, 'http://iiif.example.org/prezi/Image/0')
        self.assertEqual(self.canvas.thumbnail[0].type, 'Image')
        self.assertEqual(self.canvas.thumbnail[0].height, 200)
