from ..skeleton import Manifest,Canvas
from ..loader import monkeypatch_schema


class Add:
    def add_canvas_to_items(self,canvas_id=None):
        canvas = Canvas(id=canvas_id,type="Canvas")
        if self.items is None:
            self.items = list()
        self.items.append(canvas)
        return canvas

   





monkeypatch_schema(Manifest, [Add])