from .skeleton import *
from .base import Base

class ManifestHelpers:
    def widest_canvas(self):
        return f"Maximum canvas width: {max([c.width for c in self.items])}"

    def tallest_canvas(self):
        return f"Maximum canvas height: {max([c.height for c in self.items])}"


class CanvasHelpers:
    def helper_function(self):
        return f"This is the canvas helper function on Canvas {self.id}"


print("Monkeypatching in prezi3_helpers.py triggered")
print("-----")
print("Manifest class bases before monkeypatch:", Manifest.__bases__)
manifest_bases = list(Manifest.__bases__)
manifest_bases.append(ManifestHelpers)
Manifest.__bases__ = tuple(manifest_bases)
print("Manifest class bases after monkeypatch:", Manifest.__bases__)
print("-----")

print("Canvas class bases before monkeypatch:", Canvas.__bases__)
canvas_bases = list(Canvas.__bases__)
canvas_bases.append(CanvasHelpers)
Canvas.__bases__ = tuple(canvas_bases)
print("Canvas class bases after monkeypatch:", Canvas.__bases__)
print("-----")
print()
