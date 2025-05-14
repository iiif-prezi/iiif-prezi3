from ..loader import monkeypatch_schema
from ..skeleton import Manifest, Range


class MakeRange:

    def make_range(self, **kwargs):
        """Create a Range and add it to the calling Collection or Range.

        Creates a new Range, adds it to the calling object and returns the newly created Range.
        Accepts keyword arguments to customize the resulting instance.
        """
        range = Range(**kwargs)
        if isinstance(self, Manifest):
            if self.structures:
                self.structures.append(range)
            else:
                self.structures = [range]
        elif isinstance(self, Range):
            self.add_item(range)
        return range


monkeypatch_schema([Manifest, Range], MakeRange)
