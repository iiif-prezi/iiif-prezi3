import uuid

from ..config.config import Config, register_config
from ..skeleton import Annotation, Canvas, Collection, Manifest, Range


class AutoConfig(Config):
    def register_on_class(self, *classes):
        self.helper.register_on_class(*classes)

    def unregister_from_class(self, *classes):
        self.helper.register_on_class(*classes)


class Auto(object):
    def __init__(self, cfg, name=""):
        self.config = cfg
        cfg.helper = self
        register_config(self, name, cfg)

    def register_on_class(self, *classes):
        for c in classes:
            if not hasattr(c, '_defaulters'):
                c._defaulters = []
            if self not in c._defaulters:
                c._defaulters.append(self)

    def unregister_from_class(self, *classes):
        for c in classes:
            if hasattr(c, '_defaulters') and self in c._defaulters:
                c._defaulters.remove(self)


class AutoIdConfig(AutoConfig):
    def __init__(self, auto_type="int", base="http://example.org/iiif/"):
        self.auto_type = auto_type
        self.base_url = base
        self.translation = {}
        self.helper = None


class AutoId(Auto):

    def __init__(self, cfg, name=""):
        super().__init__(cfg, name)
        self._auto_id_int = 0
        self._auto_id_types = {}

    def generate_id(self, what, auto_type=None):
        if auto_type is None:
            auto_type = self.config.auto_type

        if auto_type == "int":
            # increment and return
            self._auto_id_int += 1
            slug = self._auto_id_int
        elif auto_type == "int-per-type":
            t = type(what).__name__
            t = self._type_translation.get(t, t)
            curr = self._auto_id_types.get(t, -1)
            curr += 1
            self._auto_id_types[t] = curr
            slug = f"{t}/{self._auto_id_types[t]}"
        elif auto_type == "uuid":
            return "urn:uuid:%s" % uuid.uuid4()
        elif auto_type == "uuid-per-type":
            t = type(what).__name__
            t = self._type_translation.get(t, t)
            slug = f"{t}/{uuid.uuid4()}"
        else:
            raise ValueError(f"Unknown auto-id type: {auto_type}")
        return self.config.base_url + str(slug)

    def generate_defaults(self, what, **kw):
        if 'id' not in kw:
            new_id = self.generate_id(what)
            return {'id': new_id}


class AutoLabelLangConfig(Config):
    def __init__(self, auto_lang="en"):
        self.auto_lang = auto_lang


class AutoLabelLang(Auto):
    def __init__(self, cfg, name=""):
        super().__init__(cfg, name)

    def generate_defaults(self, what, **kw):
        if 'label' in kw and type(kw['label']) == str:
            return {'label': {self.config.auto_lang: [kw['label']]}}


aicfg = AutoIdConfig()
alcfg = AutoLabelLangConfig()
ai = AutoId(aicfg)
al = AutoLabelLang(alcfg)

# Set up some obvious defaults
ai.register_on_class(Collection, Manifest, Canvas, Range, Annotation)
al.register_on_class(Collection, Manifest, Canvas, Range)
