from ..loader import monkeypatch_schema
from ..skeleton import Manifest

DEFAULT_CONTEXT = "http://iiif.io/api/presentation/3/context.json"


class AddContext:
    def add_context(self, context):
        """Add an extension context URI, ensuring the default IIIF Presentation 3 context is always last.

        Args:
            context (str): A context URI to add.
        """
        if self.context is None:
            self.context = [context, DEFAULT_CONTEXT]
        elif isinstance(self.context, list):
            # Always insert before the default context
            self.context.insert(-1, context)
            self.context = self.context
        else:
            self.context = [context, self.context]


monkeypatch_schema(Manifest, AddContext)
