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

