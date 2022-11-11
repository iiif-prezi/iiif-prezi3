from ..loader import monkeypatch_schema
from ..skeleton import (Canvas, Collection, KeyValueString, LngString,
                        Manifest, Range)


class AddMetadata:

    def add_metadata(self, label, value):
        # Validate incoming data
        criteria = [
            label and value,
            type(label) is type(value),
            type(label) in [str, dict, LngString]
        ]
        for c in criteria:
            if not c:
                raise TypeError

        # First ensure metadata array exists
        if not self.metadata:
            self.metadata = []

        # Add any valid metadata supplied (of the various allowed types)
        if label and value:
            if type(label) is str and type(value) is str:
                kv = KeyValueString(label=label, value=value)
                self.metadata.append(kv)

            elif type(label) is dict and type(value) is dict:
                kv = KeyValueString(
                    label=label, value=value
                )
                self.metadata.append(kv)

            elif type(label) is LngString and type(value) is LngString:
                kv = KeyValueString(label=label, value=value)
                self.metadata.append(kv)


monkeypatch_schema([Collection, Manifest, Canvas, Range], AddMetadata)
