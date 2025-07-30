import unittest

from iiif_prezi3 import (Annotation, AnnotationCollection, AnnotationPage,
                         Canvas, Collection, Manifest, Range, AnnotationBody,
                         ServiceV3, ServiceV2)


class AddServiceTest(unittest.TestCase):
    """Test if valid IIIF object can accept service 2 and 3."""

    def setUp(self):
        self.serviceID = 'https://example.org/service'
        self.serviceType = 'ImageService3'
        self.canvas = Canvas()
        self.collection = Collection()
        self.annotation = Annotation(target='https://example.org/iiif/book1/page1')
        self.annotationPage = AnnotationPage()
        self.manifest = Manifest(label='test label')
        self.range = Range()
        self.annotationCollection = AnnotationCollection()
        self.AnnotationBody = AnnotationBody(id=self.serviceID, type=self.serviceType)
        self.service3 = ServiceV3(id=self.serviceID, type=self.serviceType)
        self.service2 = ServiceV2(id=self.serviceID, type=self.serviceType)

    def test_add_service_to_Collection(self):
        self.canvas.add_service(self.service2)
        self.canvas.add_service(self.service3)

    def test_add_service_to_Manifest(self):
        self.collection.add_service(self.service3)

    def test_add_service_to_Canvas(self):
        self.annotation.add_service(self.service3)

    def test_add_service_to_Annotation(self):
        self.annotationPage.add_service(self.service3)

    def test_add_service_to_AnnotationPage(self):
        self.manifest.add_service(self.service3)

    def test_add_service_to_Range(self):
        self.range.add_service(self.service3)

    def test_add_service_to_AnnotationCollection(self):
        self.annotationCollection.add_service(self.service3)

    def test_add_service_to_AnnotationBody(self):
        self.AnnotationBody.add_service(self.service3)

    def test_get_service2_from_Collection(self):
        self.canvas.add_service(self.service2)
        self.assertEqual(self.canvas.service[0], self.service2)

    def test_get_service3_from_Collection(self):
        self.canvas.add_service(self.service3)
        self.assertEqual(self.canvas.service[0], self.service3)

    def test_add_wrong_object_to_service(self):
        with self.assertRaises(TypeError):
            self.canvas.add_service(self.manifest)
