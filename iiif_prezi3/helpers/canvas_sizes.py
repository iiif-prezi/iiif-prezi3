from ..prezi3_skeletons import Manifest
from ..prezi3_loader import monkeypatch_schema


class MaxHelper:
    def widest_canvas(self):
        return f"Maximum canvas width: {max([c.width for c in self.items])}"

    def tallest_canvas(self):
        return f"Maximum canvas height: {max([c.height for c in self.items])}"


class MinHelper:
    def thinnest_canvas(self):
        return f"Minimum canvas width: {min([c.width for c in self.items])}"

    def shortest_canvas(self):
        return f"Minimum canvas height: {min([c.height for c in self.items])}"


monkeypatch_schema(Manifest, [MaxHelper, MinHelper])

# manifest_bases = list(Manifest.__bases__)
# manifest_bases.append(MaxHelper)
# manifest_bases.append(MinHelper)
# Manifest.__bases__ = tuple(manifest_bases)