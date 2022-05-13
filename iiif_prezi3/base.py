from pydantic import BaseModel


class Base(BaseModel):

    class Config:
        validate_assignment = True

    def __getattribute__(self, prop):
        val = super(Base, self).__getattribute__(prop)
        # __root__ is a custom pydantic thing
        if hasattr(val, '__root__'):
            return str(val.__root__)
        else:
            return val

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

    def __setattr__(self, key, value):
        # look for a defaulter to manipulate the value
        if hasattr(self.__class__, '_defaulters'):
            for df in self.__class__._defaulters:
                if df.manipulates(key):
                    new = df.manipulate_value(self, value)
                    if new:
                        value = new
                        break

        # and now pass upwards for pydantic to validate and set
        super().__setattr__(key, value)
