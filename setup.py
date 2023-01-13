import os
# read the contents of your README file
from pathlib import Path

from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

if os.path.exists("version.txt"):
    VERSION = (this_directory / "version.txt").read_text().strip()
else:
    VERSION = "local_test_version"

REQUIREMENTS = [
    "pydantic >= 1.9.2, <2.0.0",
    "requests >=2.28.0, <3.0.0",
    "Pillow >=9.1.1, <10.0.0"
]

DOCS_REQUIREMENTS = [
    "mkdocs >=1.4.0, <2.0.0",
    "mkdocs-material >=8.0.0, <9.0.0",
    "mkdocstrings-python >=0.7.0, <1.0.0",
    "griffe >=0.25.2, <1.0.0",
    "mkdocs-awesome-pages-plugin >=2.8.0, <3.0.0"
]

DEV_REQUIREMENTS = [
    "autopep8 >=1.6.0, <2.0.0",
    "isort >=5.10.1, <6.0.0",
    "flake8 >=4.0.1, <5.0.0",
    "flake8-docstrings >=1.6.0, <2.0.0",
    "flake8-isort >=4.1.1, <5.0.0",
    "tox >=3.25.0, <4.0.0",
    "Pillow >=9.1.1, <10.0.0",
    "deepdiff >=6.2.2, <7.0.0"
]

# Setting up
setup(
    name="iiif-prezi3",
    version=VERSION,
    author="IIIF Prezi3 Team",
    description="IIIF Presentation v3 API implementation",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['iiif_prezi3', 'iiif_prezi3.helpers', 'iiif_prezi3.extensions', 'iiif_prezi3.config'],
    package_data={
        'iiif_prezi3': ['config/extensions.json']
    },
    classifiers=["Development Status :: 5 - Production/Stable",
                 "Intended Audience :: Developers",
                 "License :: OSI Approved :: Apache Software License",
                 "Operating System :: OS Independent",  # is this true? know Linux & OS X ok
                 "Programming Language :: Python",
                 "Programming Language :: Python :: 3",
                 "Programming Language :: Python :: 3.7",
                 "Programming Language :: Python :: 3.8",
                 "Programming Language :: Python :: 3.9",
                 "Programming Language :: Python :: 3.10",
                 "Programming Language :: Python :: 3.11",
                 "Topic :: Internet :: WWW/HTTP",
                 "Topic :: Multimedia :: Graphics :: Graphics Conversion",
                 "Topic :: Software Development :: Libraries :: Python Modules",
                 "Environment :: Web Environment"],
    python_requires='>=3',
    url='https://github.com/iiif-prezi/iiif-prezi3',
    license='Apache License, Version 2.0',
    install_requires=REQUIREMENTS,
    extras_require={
        "docs": DOCS_REQUIREMENTS,
        "dev": DEV_REQUIREMENTS,
    },
)
