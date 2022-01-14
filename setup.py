from setuptools import setup

VERSION = '0.0.2.3'
REQUIREMENTS = [
    "pydantic"
]

# Setting up
setup(
    name='iiif-prezi3',
    version=VERSION,
    author='IIIF Prezi3 Team',
    packages=['iiif_prezi3', 'iiif_prezi3.helpers', 'iiif_prezi3.extensions'],
    package_data = {
        'iiif_prezi3': ['config/extensions.json']
    },
    classifiers=["Development Status :: 4 - Beta",
                 "Intended Audience :: Developers",
                 "License :: OSI Approved :: Apache Software License",
                 "Operating System :: OS Independent",  # is this true? know Linux & OS X ok
                 "Programming Language :: Python",
                 "Programming Language :: Python :: 3",
                 "Programming Language :: Python :: 3.7",
                 "Programming Language :: Python :: 3.8",
                 "Programming Language :: Python :: 3.9",
                 "Programming Language :: Python :: 3.10",
                 "Topic :: Internet :: WWW/HTTP",
                 "Topic :: Multimedia :: Graphics :: Graphics Conversion",
                 "Topic :: Software Development :: Libraries :: Python Modules",
                 "Environment :: Web Environment"],
    url='https://github.com/iiif-prezi/iiif-prezi3',
    license='LICENSE',
    description='IIIF Presentation v3 API implementation',
    install_requires=REQUIREMENTS
)
