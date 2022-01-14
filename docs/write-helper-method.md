# Helper methods

Helper methods in `iiif-prezi3` allow functionality for common use cases to be included in the package. Helpers that are general can be loaded and used by the user as required, and those that target specific schema objects (e.g a helper to add a Canvas to a Manifest) are monkeypatched onto the relevant schema class at load time.

## Location and structure
Helper methods should be located in Python files inside the `helpers/` directory. Direct helper methods that take schema objects as arguments can be singular functions, whereas those which are designed to add new functions or properties to existing schema classes must themselves be containing inside a class, to enable them to be monkeypatched in correctly.

## Accessing Schema Objects
Relevant schema classes can be loaded from the `skeleton.py` file in the main `iiif-prezi3` package by using a relative import:
```python
from ..skeleton import Manifest
```

## Monkeypatching onto Schema classes
If the helper targets a class from the main IIIF Presentation 3 schema, then it can be monkeypatched onto that class at runtime using the `iiif_prezi3.loader.monkeypatch_schema()` method.
This function takes two arguments: the class to target, and the class(es) containing the helper methods, either as a single object or a list. Add the monkeypatch function call at the end of your helper file, and it will be run when the helper file is imported by the main package (as detailed below).

```python
from ..skeleton import Manifest
from ..loader import monkeypatch_schema


class MyHelper:
    def helper_function(self):
        return "I am a Manifest helper"

monkeypatch_schema(Manifest, MyHelper)
```


## Including helpers in the main package
To enable a helper, import it via relative import in the `helpers/__init__.py` file. This will include the functions directly in the namespace of `iiif_prezi3.helpers`, which in turn is imported in its entirety by the `__init__.py` file of the main package.

In `helpers/__init__.py`:
```python
from .example_helper import MyHelper
```

Allowing:
```
>>> from iiif_prezi3 import Manifest
>>> m = Manifest(id="https://example.com/manifest", type="Manifest", label={"en":"Example Manifest"})
>>> m.helper_function()
'I am a Manifest helper'
```


