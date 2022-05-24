from scrapper import Scrapper

HEARTSTOPPER1_ENDPOINT = "https://booksvooks.com/nonscrolablepdf/heartstopper-volume-one-pdf-alice-oseman.html"
HEARTSTOPPER2_ENDPOINT = "https://booksvooks.com/nonscrolablepdf/heartstopper-volume-two-pdf-alice-oseman.html"
HEARTSTOPPER3_ENDPOINT = "https://booksvooks.com/nonscrolablepdf/heartstopper-volume-three-pdf-alice-oseman.html"

scrapper = Scrapper()
scrapper.download_all_pages_from_volume(volume=1, url=HEARTSTOPPER1_ENDPOINT)
scrapper.download_all_pages_from_volume(volume=2, url=HEARTSTOPPER2_ENDPOINT)
scrapper.download_all_pages_from_volume(volume=3, url=HEARTSTOPPER3_ENDPOINT)
