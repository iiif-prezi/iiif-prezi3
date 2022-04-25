import sys
import unittest

import iiif_prezi3

sys.path.insert(1, '.')


# class NotCalledTest(unittest.TestCase):
#     def test_no_call(self):
#         self.assertNotIn('example_extension', dir(iiif_prezi3.extensions))

class NoArgumentsTest(unittest.TestCase):
    def test_no_arguments(self):
        iiif_prezi3.load_bundled_extensions()
        self.assertIn('example_extension', dir(iiif_prezi3.extensions))

# class ListArgumentsTest(unittest.TestCase):
#     def test_list_arguments(self):
#         iiif_prezi3.load_bundled_extensions(['example_extension'])
#         self.assertIn('example_extension', dir(iiif_prezi3.extensions))


if __name__ == '__main__':
    unittest.main()
