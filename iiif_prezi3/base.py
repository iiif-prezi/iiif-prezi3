from pydantic import BaseModel


class Base(BaseModel):
    def __getattribute__(self, prop):
        val = super(Base, self).__getattribute__(prop)
        if hasattr(val, '__root__'):
            return str(val.__root__)
        else:
            return val

