from ..skeleton import Manifest, Collection, Canvas

class AutoId(object):
    def generate_defaults(self, what, **kw):
        if not 'id' in kw:
            return {'id': "http://foo.bar.com/"}

class AutoType(object):
    def generate_defaults(self, what, **kw):
        if not 'type' in kw:
            return {'type': what.__class__.__name__}

class AutoLabelLang(object):
    def generate_defaults(self, what, **kw):
        if 'label' in kw and type(kw['label']) == str:
            return {'label': {'en': [kw['label']]}}


ai = AutoId()
at = AutoType()
al = AutoLabelLang()
Collection.defaulters = [ai, at, al]
Manifest.defaulters =[ai, at, al]
Canvas.defaulters = [ai, at, al]

