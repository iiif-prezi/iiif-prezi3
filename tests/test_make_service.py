import unittest

from iiif_prezi3 import (Annotation, AnnotationCollection, AnnotationPage,
                         Canvas, Collection, Manifest, Range, ResourceItem,
                         ServiceItem, ServiceItem1)


class MakeServiceTest(unittest.TestCase):
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
        self.resourceItem = ResourceItem(id=self.serviceID, type=self.serviceType)
        self.service3 = ServiceItem(id=self.serviceID, type=self.serviceType)
        self.service2 = ServiceItem1(id=self.serviceID, type=self.serviceType)

    def test_make_service_to_Collection(self):
        self.canvas.make_service(self.serviceID, self.serviceType)
        self.canvas.make_service(self.serviceID, self.serviceType, version=2)

    def test_make_service_to_Manifest(self):
        self.collection.make_service(self.serviceID, self.serviceType, version=2)

    def test_make_service_to_Canvas(self):
        self.annotation.make_service(self.serviceID, self.serviceType, version=2)

    def test_make_service_to_Annotation(self):
        self.annotationPage.make_service(self.serviceID, self.serviceType, version=2)

    def test_make_service_to_AnnotationPage(self):
        self.manifest.make_service(self.serviceID, self.serviceType, version=2)

    def test_make_service_to_Range(self):
        self.range.make_service(self.serviceID, self.serviceType, version=2)

    def test_make_service_to_AnnotationCollection(self):
        self.annotationCollection.make_service(self.serviceID, self.serviceType, version=2)

    def test_make_service_to_ResourceItem(self):
        self.resourceItem.make_service(self.serviceID, self.serviceType, version=2)

    def test_service2_is_service2(self):
        service2 = self.canvas.make_service(self.serviceID, self.serviceType, version=2)
        self.assertEqual(service2, self.service2)

    def test_service3_is_service3(self):
        service3 = self.canvas.make_service(self.serviceID, self.serviceType)
        self.assertEqual(service3, self.service3)

    def test_wrong_version(self):
        with self.assertRaises(ValueError):
            self.canvas.make_service(self.serviceID, self.serviceType, version=0)
