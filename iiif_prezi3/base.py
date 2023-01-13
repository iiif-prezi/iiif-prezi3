import json

from pydantic import AnyUrl, BaseModel
from pydantic.json import pydantic_encoder


class Base(BaseModel):

    class Config:
        validate_assignment = True
        validate_all = True
        copy_on_model_validation = False
        smart_union = True
        # Allow us to use the field name like service.id rather than service.@id
        allow_population_by_field_name = True

    def __getattribute__(self, prop):
        val = super(Base, self).__getattribute__(prop)
        # __root__ is a custom pydantic thing
        if hasattr(val, '__root__'):
            if type(val.__root__) in [AnyUrl]:
                # cast it to a string
                return str(val.__root__)
            else:
                return val.__root__
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

    def json(self, **kwargs):
        return self.jsonld(**kwargs)

    def jsonld(self, **kwargs):
        # approach 6- use the pydantic .dict() function to get the dict with pydantic options, add the context at the top and dump to json with modified kwargs
        excluded_args = ["exclude_unset", "exclude_defaults", "exclude_none", "by_alias"]
        pydantic_args = ["include", "exclude", "encoder"]
        dict_kwargs = dict([(arg, kwargs[arg]) for arg in kwargs.keys() if arg in pydantic_args])

        json_kwargs = dict([(arg, kwargs[arg]) for arg in kwargs.keys() if arg not in pydantic_args + excluded_args])
        return json.dumps({"@context": "http://iiif.io/api/presentation/3/context.json",
                           **self.dict(exclude_unset=False, exclude_defaults=False, exclude_none=True, by_alias=True, **dict_kwargs)}, default=pydantic_encoder, **json_kwargs)

    def jsonld_dict(self, **kwargs):
        pydantic_args = ["include", "exclude", "encoder"]
        dict_kwargs = dict([(arg, kwargs[arg]) for arg in kwargs.keys() if arg in pydantic_args])

        return {"@context": "http://iiif.io/api/presentation/3/context.json",
                **self.dict(exclude_unset=False, exclude_defaults=False, exclude_none=True, by_alias=True, **dict_kwargs)}
