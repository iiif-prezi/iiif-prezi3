import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import call, patch

from iiif_prezi3.loader import load_bundled_extensions


class ExtensionLoaderTest(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.config = Path(self.directory.name) / "extensions.json"
        self.config.write_text(json.dumps(["example_extension"]), encoding="utf-8")

    @patch("iiif_prezi3.loader.load_extension")
    def test_string_config_path_loads_extensions(self, load_extension):
        load_bundled_extensions(str(self.config))
        load_extension.assert_called_once_with("iiif_prezi3.extensions.example_extension")

    @patch("iiif_prezi3.loader.load_extension")
    def test_path_config_loads_extensions(self, load_extension):
        load_bundled_extensions(self.config)
        load_extension.assert_called_once_with("iiif_prezi3.extensions.example_extension")

    @patch("iiif_prezi3.loader.load_extension")
    def test_list_loads_each_extension(self, load_extension):
        load_bundled_extensions(["example_extension", "another_extension"])
        self.assertEqual(load_extension.call_args_list, [
            call("iiif_prezi3.extensions.example_extension"),
            call("iiif_prezi3.extensions.another_extension"),
        ])

    @patch("iiif_prezi3.loader.load_extension")
    def test_default_config_loads_extensions(self, load_extension):
        load_bundled_extensions()
        load_extension.assert_called_once_with("iiif_prezi3.extensions.example_extension")

    @patch("iiif_prezi3.loader.load_extension")
    def test_missing_config_does_not_load_extensions(self, load_extension):
        load_bundled_extensions(str(self.config.with_name("missing.json")))
        load_extension.assert_not_called()


if __name__ == "__main__":
    unittest.main()
