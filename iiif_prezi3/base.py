from pydantic import BaseModel


class Base(BaseModel):

    def __init__(self, **kw):
        # Manipulate kw via defaulter helpers
        if hasattr(self.__class__, '_defaulters'):
            for df in self.__class__._defaulters:
                update = df.generate_defaults(self, **kw)
                if update:
                    kw.update(update)
        else:
            self.__class__._defaulters = []
        super().__init__(**kw)


    def __getattribute__(self, prop):
        val = super(Base, self).__getattribute__(prop)
        if hasattr(val, '__root__'):
            return str(val.__root__)
        else:
            return val