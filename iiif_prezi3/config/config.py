

configs = {}


# FIXME: Can this just be configs.__setitem__ ?
def register_config(what, name, config):
    m = what.__class__.__module__
    n = what.__class__.__name__
    m = m.replace('iiif_prezi3.', '')
    if name:
        name = f"/{name}"
    whatname = f"{m}.{n}{name}"

    if whatname in configs:
        # allow replacement ONLY if the class is the same
        # otherwise properties won't exist
        if configs[whatname].__class__ == config.__class__:
            configs[whatname] = config
        else:
            raise ValueError("Cannot replace config with a different class")
    else:
        configs[whatname] = config


class Config(object):

    def __init__(self, **kw):
        self._values = kw.get('values', [])

    def list_fields(self):
        return list(self.__dict__.keys())
