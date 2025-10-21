import json

from pydantic import AnyUrl, BaseModel, ConfigDict

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
    class Base(BaseModel):
        model_config = ConfigDict(
            validate_assignment=True,
            # validate_all removed in v2 - now default behavior
            # copy_on_model_validation removed in v2
            # smart_union removed in v2 - now default behavior
            populate_by_name=True,  # replaces allow_population_by_field_name
        )

    def __getattribute__(self, prop):
        try:
            val = super(Base, self).__getattribute__(prop)
        except AttributeError:
            super_fields = super(Base, self).__getattribute__("model_fields")  # Changed from __fields__
            if "__root__" in super_fields:
                obj = super(Base, self).__getattribute__("__root__")
                val = super(Base, obj).__getattribute__(prop)
            else:
                raise

                # __root__ handling remains similar
        if hasattr(val, '__root__'):
            if type(val.__root__) in [AnyUrl]:
                return str(val.__root__)
            else:
                return val.__root__
        else:
            return val

    def __init__(self, **kw):
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
        # v2 uses model_dump() instead of dict()
        dict_out = self.model_dump(
            exclude_unset=False,
            exclude_defaults=False,
            exclude_none=True,
            by_alias=True,
            mode='json'  # v2 requires explicit mode
        )

        if not exclude_context:
            dict_out = {
                "@context": "http://iiif.io/api/presentation/3/context.json",
                **dict_out
            }

            # v2 uses model_dump_json() or json.dumps with default serializer
        return json.dumps(dict_out, ensure_ascii=False)

    def jsonld(self, **kwargs):
        return self.json(exclude_context=False, **kwargs)

    def jsonld_dict(self, **kwargs):
        return {
            "@context": "http://iiif.io/api/presentation/3/context.json",
            **self.model_dump(
                exclude_unset=False,
                exclude_defaults=False,
                exclude_none=True,
                by_alias=True
            )
        }
