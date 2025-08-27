import requests

from ..loader import monkeypatch_schema
from ..skeleton import Canvas, Resource, AnnotationBody


class SetHwdFromIIIF:
    # should probably be added to canvas helpers

    def set_hwd_from_iiif(self, url):
        """Set height and width on a Canvas object.

        Requests IIIF Image information remotely for an
        image resource and sets resulting height and width.
        This method will return the info.json

        Args:
            url (str): An HTTP URL for the IIIF image endpoint.
        """
        # resource url may or may not end with info.json;
        # add if not present
        if not url.endswith("info.json"):
            url = f"{url.rstrip('/')}/info.json"

        response = requests.get(url)
        # if response is not 200, raise exception
        if response.status_code != requests.codes.ok:
            response.raise_for_status()
        # if response is not valid json, request will raise
        # requests.exceptions.JSONDecodeError
        # — handle or document and let calling code handle?
        resource_info = response.json()
        self.set_hwd(resource_info.get("height"), resource_info.get("width"))

        return resource_info


monkeypatch_schema([Canvas, Resource, AnnotationBody], SetHwdFromIIIF)
