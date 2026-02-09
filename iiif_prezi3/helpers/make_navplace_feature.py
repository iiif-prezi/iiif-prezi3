from ..loader import monkeypatch_schema
from ..skeleton import (AccompanyingCanvas, Canvas, Collection, Manifest,
                        NavPlace, PlaceholderCanvas)


class MakeNavPlaceFeature:
    def make_feature(self, id=None, label=None, geometry=None, properties=None) -> dict:
        """Build a GeoJSON Feature dict and append it to this NavPlace's features.

        Args:
            id (str, optional): The Feature id.
            label (dict, optional): A label dict to merge into properties.
            geometry (dict, optional): A GeoJSON geometry dict.
            properties (dict, optional): Additional properties for the Feature.

        Returns:
            dict: The newly-created Feature dict.
        """
        feature = {"type": "Feature"}
        if id is not None:
            feature["id"] = id

        merged_properties = dict(properties) if properties else {}
        if label is not None:
            merged_properties["label"] = label
        if merged_properties:
            feature["properties"] = merged_properties

        if geometry is not None:
            feature["geometry"] = geometry

        if self.features is None:
            self.features = []
        self.features.append(feature)
        return feature


class AddNavPlaceFeature:
    def add_navplace_feature(self, id=None, label=None, geometry=None,
                             properties=None, feature_collection_id=None) -> dict:
        """Create a NavPlace (if needed) and add a GeoJSON Feature to it.

        Args:
            id (str, optional): The Feature id.
            label (dict, optional): A label dict to merge into properties.
            geometry (dict, optional): A GeoJSON geometry dict.
            properties (dict, optional): Additional properties for the Feature.
            feature_collection_id (str, optional): The id for the NavPlace FeatureCollection.

        Returns:
            dict: The newly-created Feature dict.
        """
        if self.navPlace is None:
            self.navPlace = NavPlace(id=feature_collection_id)
        return self.navPlace.make_feature(id=id, label=label, geometry=geometry,
                                          properties=properties)


monkeypatch_schema(NavPlace, MakeNavPlaceFeature)
monkeypatch_schema(
    [Collection, Manifest, Canvas, AccompanyingCanvas, PlaceholderCanvas],
    AddNavPlaceFeature
)
