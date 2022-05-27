import unittest

from iiif_prezi3 import Annotation, AnnotationPage, Manifest


class AnnotationHelpersTests(unittest.TestCase):

    def test_manifest_add_annotation(self):
        anno_target = 'http://iiif.example.org/prezi/Canvas/0'
        anno = Annotation(target=anno_target)
        m = Manifest(id='http://iiif.example.org/prezi/Manifest/0', label={'en': ['Test Manifest']})
        m.add_annotation(anno)
        # test
        self.assertEqual(len(m.annotations), 1)
        anno_page = m.annotations[0]
        self.assertTrue(isinstance(anno_page, AnnotationPage), '`annotations` should contain an AnnotationPage')
        self.assertEqual(len(anno_page.items), 1)
        # self.assertEqual(anno_page.items[0].id, 'http://iiif.example.org/prezi/Annotation/0')
        self.assertEqual(anno_page.items[0].target, anno_target)
        # self.assertEqual(anno_page.items[0].dict()["body"]["id"], 'http://iiif.example.org/prezi/Image/0')

    def test_manifest_make_annotation(self):
        anno_target = 'http://iiif.example.org/prezi/Canvas/0'
        m = Manifest(id='http://iiif.example.org/prezi/Manifest/0', label={'en': ['Test Manifest']})
        anno = m.make_annotation(target=anno_target)
        # test
        self.assertTrue(isinstance(anno, Annotation), 'returned annotation should be an Annotation')
        self.assertEqual(len(m.annotations), 1)
        anno_page = m.annotations[0]
        self.assertTrue(isinstance(anno_page, AnnotationPage), '`annotations` should contain an AnnotationPage')
        self.assertEqual(len(anno_page.items), 1)
        # self.assertEqual(anno_page.items[0].id, 'http://iiif.example.org/prezi/Annotation/0')
        self.assertEqual(anno_page.items[0].target, anno_target)
        # self.assertEqual(anno_page.items[0].dict()["body"]["id"], 'http://iiif.example.org/prezi/Image/0')
