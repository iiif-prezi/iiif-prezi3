# Generating the Schema

Install the datamodl-codegen program which will convert a JSON schema into python code. Either follow the instructions [here](https://pydantic-docs.helpmanual.io/datamodel_code_generator/) or run:

```
pip install datamodel-code-generator
```

Then run:

```
python utils/regenerate_skeleton.py 
```

This will replace the [skeleton.py](https://github.com/iiif-prezi/iiif-prezi3/blob/main/iiif_prezi3/skeleton.py) file with a newly generated one. Use this script rather than running datamodel_code_gen directly because this regenreate_skeleton code makes some changes to the schema before converting and also adds some fixes to skeleton json.  

The options for regenerate_skeleton.py can be seen below:

```
python utils/regenerate_skeleton.py -h
usage: regenerate_skeleton.py [-h] [--branch BRANCH] [--yes]

Prezi3 Skeleton regeneration

options:
  -h, --help       show this help message and exit
  --branch BRANCH  IIIF presentation-validator branch to get the schema from
  --yes, -y        Skip warning about replacing Skeleton
```

