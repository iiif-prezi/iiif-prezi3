# Viewing direction and Its Effect on Navigation
|                        | **Cookbook URLs**                                                                                                                                                          |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Recipe:**            | [https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction/](https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction/)                                   |
| **JSON-LD Example 1:** | [https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction/manifest-rtl.json](https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction/manifest-rtl.json) |
| **JSON-LD Example 2:** | [https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction/manifest-ttb.json](https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction/manifest-ttb.json) |

### Method 1 - Setting the `viewingDirection` property during object construction
#### Example 1
```python
from iiif_prezi3 import Manifest, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"

manifest = Manifest(id="https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction/manifest-rtl.json",
                    label="Book with Right-to-Left Viewing Direction",
                    summary="Playbill for \"Akiba gongen kaisen-banashi,\" \"Futatsu chōchō kuruwa nikki\" and \"Godairiki koi no fūjime\" performed at the Chikugo Theater in Osaka from the fifth month of Kaei 2 (May, 1849); main actors: Gadō Kataoka II, Ebizō Ichikawa VI, Kitō Sawamura II, Daigorō Mimasu IV and Karoku Nakamura I; on front cover: producer Mominosuke Ichikawa's crest.",
                    viewingDirection="right-to-left")

canvas1 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/4f92cceb12dd53b52433425ce44308c7-ucla_bib1987273_no001_rs_001",
                                         id="https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction/canvas/p1",
                                         label="front cover")
canvas1.items[0].id = "https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction/page/p1/1"
canvas1.items[0].items[0].id = "https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction/annotation/p0001-image"

canvas2 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/4f92cceb12dd53b52433425ce44308c7-ucla_bib1987273_no001_rs_002",
                                         id="https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction/canvas/p2",
                                         label="pages 1-2")
canvas2.items[0].id = "https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction/page/p2/1"
canvas2.items[0].items[0].id = "https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction/annotation/p0002-image"

canvas3 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/4f92cceb12dd53b52433425ce44308c7-ucla_bib1987273_no001_rs_003",
                                         id="https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction/canvas/p3",
                                         label="pages 3-4")
canvas3.items[0].id = "https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction/page/p3/1"
canvas3.items[0].items[0].id = "https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction/annotation/p0003-image"

canvas4 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/4f92cceb12dd53b52433425ce44308c7-ucla_bib1987273_no001_rs_004",
                                         id="https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction/canvas/p4",
                                         label="pages 5-6")
canvas4.items[0].id = "https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction/page/p4/1"
canvas4.items[0].items[0].id = "https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction/annotation/p0004-image"

canvas5 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/4f92cceb12dd53b52433425ce44308c7-ucla_bib1987273_no001_rs_005",
                                         id="https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction/canvas/p5",
                                         label="back cover")
canvas5.items[0].id = "https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction/page/p5/1"
canvas5.items[0].items[0].id = "https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction/annotation/p0005-image"

print(manifest.json(indent=2))
```

#### Example 2
```python
from iiif_prezi3 import Manifest, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"

manifest = Manifest(id="https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction/manifest-ttb.json",
                    label="Diary with Top-to-Bottom Viewing Direction",
                    summary="William Lewis Sachtleben was an American long-distance cyclist who rode across Asia from Istanbul to Peking in 1891 to 1892 with Thomas Gaskell Allen Jr., his classmate from Washington University. This was part of a longer journey that began the day after they had graduated from college, when they travelled to New York and on to Liverpool; in all they travelled 15,044 miles by bicycle, 'the longest continuous land journey ever made around the world' as reported in their book <cite>Across Asia on a bicycle</cite> (1895). Sachtleben documented his travels with photographs and diaries, the latter of which he numbered sequentially. The diary of notebook 'No. 10' covers a portion of their journey through the Armenian area of Turkey from April 12 to May 9 (there is a 2-page reading list at the end). During this time they rode from Ankara (Angora in the diary) to Sivas, where they stayed for ten days while Allen had a bout of typhoid fever, and the first half of a ten-day excursion to Merzifon (Mersovan in the diary), taken by Sachtleben to give Allen additional time to recover.",
                    viewingDirection="top-to-bottom")
canvas1 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/9ee11092dfd2782634f5e8e2c87c16d5-uclamss_1841_diary_07_02",
                                         id="https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction/canvas/v1",
                                         label="image 1")
canvas1.items[0].id = "https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction/page/v1/1"
canvas1.items[0].items[0].id = "https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction/annotation/v0001-image"

canvas2 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/9ee11092dfd2782634f5e8e2c87c16d5-uclamss_1841_diary_07_03",
                                         id="https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction/canvas/v2",
                                         label="image 2")
canvas2.items[0].id = "https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction/page/v2/1"
canvas2.items[0].items[0].id = "https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction/annotation/v0002-image"

canvas3 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/9ee11092dfd2782634f5e8e2c87c16d5-uclamss_1841_diary_07_04",
                                         id="https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction/canvas/v3",
                                         label="image 3")
canvas3.items[0].id = "https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction/page/v3/1"
canvas3.items[0].items[0].id = "https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction/annotation/v0003-image"

canvas4 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/9ee11092dfd2782634f5e8e2c87c16d5-uclamss_1841_diary_07_05",
                                         id="https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction/canvas/v4",
                                         label="image 4")
canvas4.items[0].id = "https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction/page/v4/1"
canvas4.items[0].items[0].id = "https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction/annotation/v0004-image"

print(manifest.json(indent=2))
```
