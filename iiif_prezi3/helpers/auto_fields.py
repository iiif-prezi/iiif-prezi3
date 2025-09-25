import uuid

from ..config.config import Config, register_config
from ..skeleton import (AnnotationPage, Canvas, Class, Homepage,
                        KeyValueString, ManifestRef, NavPlace, Provider,
                        Range, Reference, AnnotationBody, ServiceV2, Manifest,
                        AnnotationCollection, AccompanyingCanvas, PlaceholderCanvas,
                        Collection)

def _find_subclasses(cls):
    seen = set()
    stack = [cls]
    while stack:
        c = stack.pop()
        if c in seen:
            continue
        seen.add(c)
        yield c
        stack.extend(c.__subclasses__())


class AutoConfig(Config):

    def __init__(self, **kw):
        self.properties = []
        Config.__init__(self, **kw)

    def register_on_class(self, *classes):
        self.helper.register_on_class(*classes)

    def unregister_from_class(self, *classes):
        self.helper.register_on_class(*classes)


class Auto(object):
    def __init__(self, cfg, name=""):
        self.config = cfg
        cfg.helper = self
        register_config(self, name, cfg)

    def register_on_class(self, *classes, include_subclasses=True):
        """Register the _defaulters class variable on the specific class.
        
        If include_subclasses=True, attach to all *existing* subclasses too.
        Otherwise, only attach to the classes passed in.
        """
        targets = []
        for c in classes:
            if include_subclasses:
                targets.extend(_find_subclasses(c))
            else:
                targets.append(c)

        for t in targets:
            # Give the *class itself* its own list (no inherited aliasing).
            if '_defaulters' not in t.__dict__:
                t._defaulters = []  # owned by this class only

            if self not in t._defaulters:
                t._defaulters.append(self)

    def unregister_from_class(self, *classes):
        for c in classes:
            if hasattr(c, '_defaulters') and self in c._defaulters:
                c._defaulters.remove(self)

    def manipulates(self, property):
        return property in self.config.properties

    def generate_defaults(self, what, **kw):
        updated = {}
        for p in self.config.properties:
            if p in kw:
                val = self.manipulate_value(what, kw[p])
            else:
                # Not present, but might still generate from scratch
                val = self.manipulate_value(what)
            if val is not None:
                updated[p] = val
        return updated

    def manipulate_value(self, what, value=None):
        # Default to noop
        return None


class AutoIdConfig(AutoConfig):
    def __init__(self, auto_type="int", base="http://example.org/iiif/"):
        self.properties = ['id']
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
            t = self.config.translation.get(t, t)
            curr = self._auto_id_types.get(t, -1)
            curr += 1
            self._auto_id_types[t] = curr
            slug = f"{t}/{self._auto_id_types[t]}"
        elif auto_type == "uuid":
            slug = str(uuid.uuid4())
        elif auto_type == "uuid-per-type":
            t = type(what).__name__
            t = self.config.translation.get(t, t)
            slug = f"{t}/{uuid.uuid4()}"
        else:
            raise ValueError(f"Unknown auto-id type: {auto_type}")
        return self.config.base_url + str(slug)

    def manipulate_value(self, what, value=None):
        if value:
            # Currently only generate from scratch
            # Future versions might allow passing the slug to be turned into a URI
            return None
        else:
            return self.generate_id(what)


class AutoLangConfig(Config):
    def __init__(self, auto_lang="none"):
        self.properties = ['label', 'value', 'summary']
        self.auto_lang = auto_lang


class AutoLang(Auto):
    def __init__(self, cfg, name=""):
        super().__init__(cfg, name)

    def manipulate_value(self, what, value=None):
        if not value:
            return None
        elif isinstance(value, str):
            return {self.config.auto_lang: [value]}
        elif isinstance(value, list):
            return {self.config.auto_lang: value}
        else:
            return None


class AutoItemsConfig(Config):
    def __init__(self):
        self.properties = ['items']


class AutoItems(Auto):
    def __init__(self, cfg, name=""):
        super().__init__(cfg, name)

    def manipulate_value(self, what, value=None):
        if not value:
            return []
        else:
            return value


class AutoListConfig(Config):
    def __init__(self):
        self.properties = ['behavior', 'service', 'services', 'features', 'thumbnail', 'logo', 'rendering', 'homepage', 'metadata',
                           'partOf', 'provider', 'seeAlso', 'annotations']


class AutoList(Auto):
    def __init__(self, cfg, name=""):
        super().__init__(cfg, name)

    def manipulate_value(self, what, value=None):
        if not value:
            return None
        if not isinstance(value, list):
            return [value]
        else:
            return value


class AutoLanguageListConfig(Config):
    def __init__(self):
        self.properties = ['language']


aicfg = AutoIdConfig()
alcfg = AutoLangConfig()
aitcfg = AutoItemsConfig()
alstcfg = AutoListConfig()
allstcfg = AutoLanguageListConfig()
ai = AutoId(aicfg)
al = AutoLang(alcfg)
ait = AutoItems(aitcfg)
alst = AutoList(alstcfg, name="General")
allst = AutoList(allstcfg, name="Language")
# Set up some obvious defaults
ai.register_on_class(AnnotationPage, Class, ManifestRef)
al.register_on_class(KeyValueString, Class, Reference, AnnotationBody, ManifestRef)
ait.register_on_class(Canvas, PlaceholderCanvas, AccompanyingCanvas, Range, AnnotationCollection, AnnotationPage, Manifest, Collection)
alst.register_on_class(Class, AnnotationPage, AnnotationBody, ServiceV2, NavPlace, Reference, Provider)
allst.register_on_class(Homepage)