from ..loader import monkeypatch_schema
from ..skeleton import Manifest, Canvas


class MakeCanvas:

    def make_canvas(self, **kwargs):
        """Add a Canvas to a Manifest.

        Creates a new Canvas, adds a Reference to it to the
        calling Manifest items and returns the newly created Canvas.
        Accepts keyword arguments to customize the resulting instance.
        """
        canvas = Canvas(**kwargs)
        self.add_item(canvas)
        return canvas


monkeypatch_schema(Manifest, MakeCanvas)
