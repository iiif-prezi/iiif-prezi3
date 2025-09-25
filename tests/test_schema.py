import json
import unittest

from pydantic import ValidationError

from iiif_prezi3 import (Annotation, AnnotationBody, ImageAPISelector,
                         Manifest, Range, ServiceV2, ServiceV3,
                         SpecificResource)


class TestSchema(unittest.TestCase):
    """Ensure schema changes have made it to iiif_prezi3."""
    base_url = "http://example.com"

    def test_mandatory_items(self):
        """If a manifest has items it should be a Manifest object, if not it should be a ManifestRef."""
        manifest = Manifest(id=f"{self.base_url}/manifest.json", label="Single Image Example")

        with self.assertRaises(ValidationError):
            manifest.items = None

    def test_extra_annotation_fields(self):
        """Annotation class should allow extra fields for Web Annotation Data Model.

        https://github.com/iiif-prezi/iiif-prezi3/issues/223
        """
        body = AnnotationBody(
            id="https://iiif.io/api/cookbook/recipe/0266-full-canvas-annotation/canvas-1/annopage-2/anno-1/body",
            type="TextualBody",
            language="de",
            format="text/plain",
            value="Göttinger Marktplatz mit Gänseliesel Brunnen"
        )

        annotation = Annotation(
            id="https://iiif.io/api/cookbook/recipe/0266-full-canvas-annotation/canvas-1/annopage-2/anno-1",
            motivation="commenting",
            creator="http://example.org/user1",
            created="2015-01-28T12:00:00Z",
            modified="2015-01-29T09:00:00Z",
            body=body,
            target="https://iiif.io/api/cookbook/recipe/0266-full-canvas-annotation/canvas-1"
        )

        self.assertTrue(hasattr(annotation, "creator"), "Creator should have made it into the annotation json")
        self.assertTrue(hasattr(annotation, "created"), "Created should have made it into the annotation json")
        self.assertTrue(hasattr(annotation, "modified"), "Modified should have made it into the annotation json")

    def test_extra_servicev3_fields(self):
        """Allow extra fields on a service.

        https://github.com/iiif-prezi/iiif-prezi3/issues/204
        """
        service = ServiceV3(id="https://fixtures.iiif.io/other/level0/Glen/photos/gottingen", type="ImageService3", profile="level0")

        service.sizes = [
            {
                "width": 126,
                "height": 95
            },
            {
                "width": 252,
                "height": 189
            },
            {
                "width": 504,
                "height": 378
            }
        ]

        self.assertTrue(hasattr(service, "sizes"), "Service should retain sizes for an image service")
        self.assertEqual(len(service.sizes), 3, "Service should be an array of 3 items.")

        self.assertTrue(hasattr(service, "profile"), "Profile should be in service")

    def test_extra_servicev2_fields(self):
        """Allow extra fields on a service."""
        service = ServiceV2(id="https://fixtures.iiif.io/other/level0/Glen/photos/gottingen", type="ImageService2", profile="level0")

        service.sizes = [
            {
                "width": 126,
                "height": 95
            },
            {
                "width": 252,
                "height": 189
            },
            {
                "width": 504,
                "height": 378
            }
        ]

        self.assertTrue(hasattr(service, "sizes"), "Service should retain sizes for an image service")
        self.assertEqual(len(service.sizes), 3, "Service should be an array of 3 items.")

        self.assertTrue(hasattr(service, "profile"), "Profile should be in service")

    def test_range_behavior(self):
        """Allow behavior on a range."""
        range = Range(id="https://example.com/range/1")
        range.label = {"en": ["Thumbnail Navigation"]}
        range.behavior = "thumbnail-nav"

        data = json.loads(range.json())
        self.assertEqual("thumbnail-nav", data["behavior"][0], "Range behavior should be retained.")

    def test_specific_resource_body(self):
        selector = ImageAPISelector(rotation=90)

        image_source = AnnotationBody(
            id="https://iiif.io/api/image/3.0/example/reference/4ce82cef49fb16798f4c2440307c3d6f-newspaper-p2/full/max/0/default.jpg",
            type="Image",
            format="image/jpeg",
            height=4999,
            width=3536,
        )

        image_source.make_service(
            id="https://iiif.io/api/image/3.0/example/reference/4ce82cef49fb16798f4c2440307c3d6f-newspaper-p2",
            type="ImageService3",
            profile="level1"
        )
        body = SpecificResource(
            id="https://iiif.io/api/cookbook/recipe/0040-image-rotation-service/body/v0001-image",
            type="SpecificResource",
            source=image_source,
            selector=selector)

        self.assertTrue(hasattr(body, "source"))
        self.assertTrue(hasattr(body, "selector"))

        annotation = Annotation(id="https://example.com", motivation="painting", body=body, target="https://iiif.io/api/cookbook/recipe/0040-image-rotation-service/canvas/p1")

        self.assertTrue(hasattr(annotation, "body"))

    def test_optional_selector(self):
        resource = SpecificResource(
            type="SpecificResource",
            source="http://www.wikidata.org/entity/Q18624915",
        )

        self.assertIsNone(resource.id, "Expected ID to be none as it hasn't been set. ")
        self.assertTrue(hasattr(resource, "type"))
        self.assertTrue(hasattr(resource, "source"))
