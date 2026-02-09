import unittest

from iiif_prezi3 import Canvas, NavPlace


class NavPlaceHelpersTest(unittest.TestCase):
    def test_make_navplace_feature(self):
        """Test that NavPlace.make_feature builds a correct Feature dict and appends it."""
        np = NavPlace(id="http://example.org/fc/1")
        feature = np.make_feature(
            id="http://example.org/feature/1",
            label={"en": ["Test Location"]},
            geometry={"type": "Point", "coordinates": [10.0, 20.0]},
        )
        self.assertEqual(feature["type"], "Feature")
        self.assertEqual(feature["id"], "http://example.org/feature/1")
        self.assertEqual(feature["properties"]["label"], {"en": ["Test Location"]})
        self.assertEqual(feature["geometry"]["type"], "Point")
        self.assertEqual(feature["geometry"]["coordinates"], [10.0, 20.0])
        self.assertEqual(len(np.features), 1)
        self.assertIs(np.features[0], feature)

    def test_add_navplace_feature(self):
        """Test that Canvas.add_navplace_feature creates NavPlace and feature in one call."""
        canvas = Canvas(id="http://example.org/canvas/1", type="Canvas",
                        label={"en": ["Test Canvas"]}, height=100, width=100)
        self.assertIsNone(canvas.navPlace)
        feature = canvas.add_navplace_feature(
            id="http://example.org/feature/1",
            label={"en": ["Test Location"]},
            geometry={"type": "Point", "coordinates": [10.0, 20.0]},
            feature_collection_id="http://example.org/fc/1",
        )
        self.assertIsNotNone(canvas.navPlace)
        self.assertEqual(canvas.navPlace.id, "http://example.org/fc/1")
        self.assertEqual(len(canvas.navPlace.features), 1)
        self.assertEqual(feature["type"], "Feature")
        self.assertEqual(feature["id"], "http://example.org/feature/1")

    def test_add_navplace_feature_multiple(self):
        """Test that multiple add_navplace_feature calls append features correctly."""
        canvas = Canvas(id="http://example.org/canvas/1", type="Canvas",
                        label={"en": ["Test Canvas"]}, height=100, width=100)
        canvas.add_navplace_feature(
            id="http://example.org/feature/1",
            label={"en": ["Location 1"]},
            geometry={"type": "Point", "coordinates": [10.0, 20.0]},
            feature_collection_id="http://example.org/fc/1",
        )
        canvas.add_navplace_feature(
            id="http://example.org/feature/2",
            label={"en": ["Location 2"]},
            geometry={"type": "Point", "coordinates": [30.0, 40.0]},
        )
        self.assertEqual(len(canvas.navPlace.features), 2)
        self.assertEqual(canvas.navPlace.features[0]["id"], "http://example.org/feature/1")
        self.assertEqual(canvas.navPlace.features[1]["id"], "http://example.org/feature/2")
        # feature_collection_id should remain from first call
        self.assertEqual(canvas.navPlace.id, "http://example.org/fc/1")
