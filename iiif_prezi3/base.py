import json

from pydantic import AnyUrl, BaseModel
from pydantic.json import pydantic_encoder

def _inherit_defaulters(cls):
    # Merge bases→derived, dedup while preserving first occurrence
    seen, defaulters = set(), []
    for base in reversed(cls.__mro__):  # bases first
        for df in base.__dict__.get('_defaulters', []):
            if df not in seen:
                seen.add(df)
                defaulters.append(df)

    return defaulters

class Base(BaseModel):
    class Config:
        validate_assignment = True
        validate_all = True
        copy_on_model_validation = 'none'
        smart_union = True
        # Allow us to use the field name like service.id rather than service.@id
        allow_population_by_field_name = True

    def __getattribute__(self, prop):
        try:
            val = super(Base, self).__getattribute__(prop)
        except AttributeError:
            super_fields = super(Base, self).__getattribute__("__fields__")
            if "__root__" in super_fields:
                obj = super(Base, self).__getattribute__("__root__")
                val = super(Base, obj).__getattribute__(prop)
            else:
                raise

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
        # Manipulate kw via defaulter helpers (merged from MRO)
        for df in _inherit_defaulters(self.__class__):
            update = df.generate_defaults(self, **kw)
            if update:
                kw.update(update)

        super().__init__(**kw)

    def __setattr__(self, key, value):
         # let defaulters manipulate the value before pydantic sets it
        for df in _inherit_defaulters(self.__class__):
            if df.manipulates(key):
                new = df.manipulate_value(self, value)
                if new:
                    value = new
                    break

        # and now pass upwards for pydantic to validate and set
        super().__setattr__(key, value)

    def json(self, exclude_context=False, **kwargs):
        # approach 6- use the pydantic .dict() function to get the dict with pydantic options, add the context at the top and dump to json with modified kwargs
        excluded_args = ["exclude_unset", "exclude_defaults", "exclude_none", "by_alias", "ensure_ascii", "default"]
        pydantic_args = ["include", "exclude", "encoder"]
        dict_kwargs = dict([(arg, kwargs[arg]) for arg in kwargs.keys() if arg in pydantic_args])

        json_kwargs = dict([(arg, kwargs[arg]) for arg in kwargs.keys() if arg not in pydantic_args + excluded_args])

        dict_out = self.dict(exclude_unset=False,
                             exclude_defaults=False,
                             exclude_none=True,
                             by_alias=True,
                             **dict_kwargs)

        if not exclude_context:
            dict_out = {"@context": "http://iiif.io/api/presentation/3/context.json",
                        **dict_out}

        return json.dumps(dict_out,
                          ensure_ascii=False,
                          default=pydantic_encoder,
                          **json_kwargs)

    def jsonld(self, **kwargs):
        return self.json(exclude_context=False, **kwargs)

    def jsonld_dict(self, **kwargs):
        pydantic_args = ["include", "exclude", "encoder"]
        dict_kwargs = dict([(arg, kwargs[arg]) for arg in kwargs.keys() if arg in pydantic_args])

        return {"@context": "http://iiif.io/api/presentation/3/context.json",
                **self.dict(exclude_unset=False, exclude_defaults=False, exclude_none=True, by_alias=True, **dict_kwargs)}
