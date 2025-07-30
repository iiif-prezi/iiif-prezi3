# Generating the Schema

Install the datamodl-codegen program which will convert a JSON schema into python code. Either follow the instructions [here](https://pydantic-docs.helpmanual.io/datamodel_code_generator/) or run:

```
pip install datamodel-code-generator
```

Then in the iiif-prezi3 code directory run:

```
datamodel-codegen --input ~/code/presentation-validator/schema/iiif_3_0.json --input-file-type jsonschema --use-default --remove-special-field-name-prefix --strict-nullable --base-class base.Base --use-title-as-name --output skeleton.py
```

Replacing the path to your iiif schema file with where ever you have downloaded the [iiif_3_0.json](https://github.com/IIIF/presentation-validator/blob/master/schema/iiif_3_0.json) file.
