from ..loader import monkeypatch_schema
from ..skeleton import Collection, Manifest


class MakeManifest:

    def make_manifest(self, **kwargs):
        """Add a Manifest to a Collection.

        Creates a new Manifest, adds a Reference to it to the
        calling Collection items and returns the newly created Manifest.
        Accepts keyword arguments to customize the resulting instance.
        """
        manifest = Manifest(**kwargs)
        self.add_item(manifest)
        return manifest


monkeypatch_schema(Collection, MakeManifest)
