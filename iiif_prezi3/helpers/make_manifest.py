from ..loader import monkeypatch_schema
from ..skeleton import Collection, ManifestRef


class MakeManifest:

    def make_manifest(self, **kwargs):
        """Add a Manifest to a Collection as a ManifestRef.

        Creates a new Manifest, adds a Reference to it to the
        calling Collection items and returns the newly created Manifest.
        Accepts keyword arguments to customize the resulting instance.
        """
        kwargs.pop('items', None)
        manifest = ManifestRef(**kwargs)
        self.add_item(manifest)
        return manifest


monkeypatch_schema(Collection, MakeManifest)
