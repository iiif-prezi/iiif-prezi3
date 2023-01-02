# Navigation by Chronology
|                                     | **Cookbook URLs** |
|-------------------------------------|-------------------|
| **Recipe:**                         | [https://iiif.io/api/cookbook/recipe/0230-navdate/](https://iiif.io/api/cookbook/recipe/0230-navdate/) |
| **JSON-LD Example 1 - 1986 Map:**   | [https://iiif.io/api/cookbook/recipe/0230-navdate/navdate_map_2-manifest.json](https://iiif.io/api/cookbook/recipe/0230-navdate/navdate_map_2-manifest.json) |
| **JSON-LD Example 2 - 1987 Map:**   | [https://iiif.io/api/cookbook/recipe/0230-navdate/navdate_map_1-manifest.json](https://iiif.io/api/cookbook/recipe/0230-navdate/navdate_map_1-manifest.json) |
| **JSON-LD Example 3 - Collection:** | [https://iiif.io/api/cookbook/recipe/0230-navdate/navdate-collection.json](https://iiif.io/api/cookbook/recipe/0230-navdate/navdate-collection.json) |

### Method 1 - Setting the `navDate` property during object construction using a `datetime` object
#### Example 1 - 1986 Map
```python
--8<-- "docs/recipes/scripts/0230-navdate-method1-example1.py"
```
#### Example 2 - 1987 Map
```python
--8<-- "docs/recipes/scripts/0230-navdate-method1-example2.py"
```
#### Example 3 - Collection
Here we can make use of the fact that `iiif-prezi3` will automatically turn a Manifest into a reference when it is added to a Collection object.
```python
--8<-- "docs/recipes/scripts/0230-navdate-method1-example3.py"
```

### Method 2 - Setting the `navDate` property with a string
#### Example 1 - 1986 Map
```python
--8<-- "docs/recipes/scripts/0230-navdate-method2-example1.py"
```
#### Example 2 - 1987 Map
```python
--8<-- "docs/recipes/scripts/0230-navdate-method2-example2.py"
```
#### Example 3 - Collection
To show the different possible approaches, here we will build the Collection object manually using the `ManifestRef` class.
```python
--8<-- "docs/recipes/scripts/0230-navdate-method2-example3.py"
```