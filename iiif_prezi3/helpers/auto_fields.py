from ..skeleton import Manifest, Collection, Canvas
import uuid

class AutoId(object):

    def __init__(self, auto_type="int", base="http://example.org/iiif/"):
        self.auto_type = auto_type    
        self.base_url = base
        self._auto_id_int = 0
        self._auto_id_types = {}
        self._type_translation = {'Manifest': 'manifest'}

    def generate_id(self, what, auto_type=None):
        if auto_type == None:
            auto_type = self.auto_type

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
        return self.base_url + str(slug)  

    def generate_defaults(self, what, **kw):
        if not 'id' in kw:
            new_id = self.generate_id(what)
            return {'id': new_id}

class AutoLabelLang(object):
    def __init__(self, auto_lang="en"):
        self._auto_lang = auto_lang

    def generate_defaults(self, what, **kw):
        if 'label' in kw and type(kw['label']) == str:
            return {'label': {self._auto_lang: [kw['label']]}}

# FIXME: Need to be able to pass in configuration
ai = AutoId(auto_type="int-per-type")
al = AutoLabelLang()
Collection.defaulters = [ai, al]
Manifest.defaulters =[ai, al]
Canvas.defaulters = [ai, al]

