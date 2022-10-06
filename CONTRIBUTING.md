# Contributing to `iiif-prezi3`

Issues and pull requests are appreciated. If you are working on a pull request please ensure you create an issue first so the implementation details can be discussed with other interested parties.

## Submitting issues

In the case of bugs please describe in detail, preferably with a link to the Manifest and/or other IIIF asset that demonstrates the problem.

If you suggest a new feature, please give an example of expected behaviour and use. For changes to modules and methods a test case would be ideal.

## Coding style

If submitting a pull request:

   * Please discuss in an issue before submitting a pull request for significant changes.
   * Follow [PEP8](https://www.python.org/dev/peps/pep-0008/) and [PEP257](https://www.python.org/dev/peps/pep-0257/). These will be required in the CI builds.
   * Don't repeat code.
   * Cover the code with tests.
   * Use [Google style docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) for any code documentation you add.

## Developing helpers

The core code for this library is auto generated using [pydantic](https://github.com/iiif-prezi/iiif-prezi3/blob/main/docs/generate-schema.md). The addition of functionality is done through the use of helpers.
To develop a helper you should follow the documentation [here](https://github.com/iiif-prezi/iiif-prezi3/blob/main/docs/write-helper-method.md) but at a minimum you need the following:

 * Helper code in the [helpers directory](https://github.com/iiif-prezi/iiif-prezi3/tree/main/iiif_prezi3/helpers)
 * A respective test for your helper in the [test directory](https://github.com/iiif-prezi/iiif-prezi3/tree/main/tests)
 * A fixture which demonstrates your use case in the [fixtures directory](https://github.com/iiif-prezi/iiif-prezi3/tree/main/tests/fixtures).

Please submit your pull request to this repository and one of the library committers will merge it into the main if it fits these requirements.


## Docs

To build and view the documentation locally, install requirements with `pip install -e '.[docs]'` and then run `mkdocs serve`.