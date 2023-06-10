from iiif_prezi3 import Manifest, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
base_url = "https://iiif.io/api/cookbook/recipe/0010-book-2-viewing-direction"

manifest = Manifest(id=f"{base_url}/manifest-ttb.json",
                    label="Diary with Top-to-Bottom Viewing Direction",
                    summary="William Lewis Sachtleben was an American long-distance cyclist who rode across Asia from Istanbul to Peking in 1891 to 1892 with Thomas Gaskell Allen Jr., his classmate from Washington University. This was part of a longer journey that began the day after they had graduated from college, when they travelled to New York and on to Liverpool; in all they travelled 15,044 miles by bicycle, 'the longest continuous land journey ever made around the world' as reported in their book <cite>Across Asia on a bicycle</cite> (1895). Sachtleben documented his travels with photographs and diaries, the latter of which he numbered sequentially. The diary of notebook 'No. 10' covers a portion of their journey through the Armenian area of Turkey from April 12 to May 9 (there is a 2-page reading list at the end). During this time they rode from Ankara (Angora in the diary) to Sivas, where they stayed for ten days while Allen had a bout of typhoid fever, and the first half of a ten-day excursion to Merzifon (Mersovan in the diary), taken by Sachtleben to give Allen additional time to recover.",
                    viewingDirection="top-to-bottom")
canvas1 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/9ee11092dfd2782634f5e8e2c87c16d5-uclamss_1841_diary_07_02",
                                         id=f"{base_url}/canvas/v1",
                                         label="image 1",
                                         anno_id=f"{base_url}/annotation/v0001-image",
                                         anno_page_id=f"{base_url}/page/v1/1")

canvas2 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/9ee11092dfd2782634f5e8e2c87c16d5-uclamss_1841_diary_07_03",
                                         id=f"{base_url}/canvas/v2",
                                         label="image 2",
                                         anno_id=f"{base_url}/annotation/v0002-image",
                                         anno_page_id=f"{base_url}/page/v2/1")

canvas3 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/9ee11092dfd2782634f5e8e2c87c16d5-uclamss_1841_diary_07_04",
                                         id=f"{base_url}/canvas/v3",
                                         label="image 3",
                                         anno_id=f"{base_url}/annotation/v0003-image",
                                         anno_page_id=f"{base_url}/page/v3/1")

canvas4 = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/9ee11092dfd2782634f5e8e2c87c16d5-uclamss_1841_diary_07_05",
                                         id=f"{base_url}/canvas/v4",
                                         label="image 4",
                                         anno_id=f"{base_url}/annotation/v0004-image",
                                         anno_page_id=f"{base_url}/page/v4/1")

print(manifest.json(indent=2))
