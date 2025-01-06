import unittest

from iiif_prezi3 import (AccompanyingCanvas, Annotation, AnnotationCollection,
                         AnnotationPage, Canvas, Collection, ExternalItem,
                         Manifest, PlaceholderCanvas, Range, ResourceItem)


class AddRenderingTest(unittest.TestCase):

    def setUp(self):
        self.base = "https://example.org/iiif"
        self.external_item = ExternalItem(format="application/pdf",
                                          id="https://fixtures.iiif.io/other/UCLA/kabuki_ezukushi_rtl.pdf",
                                          type="Text")
        self.canvas = Canvas(id=f"{self.base}/canvas/1")
        self.annotation = Annotation(target=f"{self.base}/canvas/1")
        self.anno_page = AnnotationPage()
        self.ac_canvas = AccompanyingCanvas(type="Canvas")
        self.ph_canvas = PlaceholderCanvas()
        self.anno_collection = AnnotationCollection()
        self.manifest = Manifest(label='test label')
        self.range = Range()
        self.resource = ResourceItem(id=f"{self.base}/resource/1", type="Image")
        self.collection = Collection()

    def test_add_rendering_to_collection(self):
        self.collection.add_rendering(self.external_item)

    def test_add_rendering_to_anno_collection(self):
        self.anno_collection.add_rendering(self.external_item)

    def test_add_rendering_to_annotation(self):
        self.annotation.add_rendering(self.external_item)

    def test_add_rendering_to_canvas(self):
        self.canvas.add_rendering(self.external_item)

    def test_add_rendering_to_annotation_page(self):
        self.anno_page.add_rendering(self.external_item)

    def test_add_rendering_to_annotation(self):
        self.annotation.add_rendering(self.external_item)

    def test_add_rendering_to_ac_canvas(self):
        self.ac_canvas.add_rendering(self.external_item)

    def test_add_rendering_to_ph_canvas(self):
        self.ph_canvas.add_rendering(self.external_item)

    def test_add_rendering_to_resource(self):
        self.resource.add_rendering(self.external_item)

    def test_add_rendering_to_manifest(self):
        self.manifest.add_rendering(self.external_item)
