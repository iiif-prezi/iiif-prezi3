## How to add references to manifest inside a collection
iif-prezi3 offer some helper methods for adding a reference to manifests and collection inside collections. Reference to manifests inside collections can not contain the items property while label, id and type are required (see [APIs](https://iiif.io/api/presentation/3.0/#51-collection) for more).

Using `iiif_prezi3` this can be done as follows:


```python
import iiif_prezi3
mycollection = iiif_prezi3.Collection(id='http://iiif.example.org/prezi/Collection/0', type='Collection')
```


```python
myrefmanifest = mycollection.add_manifest_reference_to_items(manifest_id='http://iiif.example.org/prezi/Manifest/0',label={'en': 'default label'})
```

This will return a a collection object with a reference to a manifest inside the `items` property:


```python
print(mycollection.json(exclude_unset=True,indent=2))
```

    {
      "id": "http://iiif.example.org/prezi/Collection/0",
      "type": "Collection",
      "items": [
        {
          "id": "http://iiif.example.org/prezi/Manifest/0",
          "label": {},
          "type": "Manifest"
        }
      ]
    }



```python

```


```python

```
