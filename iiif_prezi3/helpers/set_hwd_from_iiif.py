from functools import lru_cache
import requests

from ..loader import monkeypatch_schema
from ..skeleton import Canvas, Resource, ResourceItem


@lru_cache(maxsize=3)
def get_info_json(url):
    """Cache the info.json response of the URL request.

    Args:
        url (str): An HTTP URL for the IIIF image endpoint.

    Returns:
        dict: The info.json as a dictionary.
    """
    response = requests.get(url)
    # if response is not 200, raise exception
    if response.status_code != requests.codes.ok:
        response.raise_for_status()
    # if response is not valid json, request will raise
    # requests.exceptions.JSONDecodeError
    # — handle or document and let calling code handle?
    return response.json()


class SetHwdFromIIIF:
    # should probably be added to canvas helpers
    def set_hwd_from_iiif(self, url, use_cache=True):
        """Set height and width on a Canvas object.

        Requests IIIF Image information remotely for an
        image resource and sets resulting height and width.
        This method will return the info.json

        Args:
            url (str): An HTTP URL for the IIIF image endpoint.
            use_cache (bool): If True multiple requests to the same URL will
            use the cached response without making new requests to the server
            (default True).
        """
        # resource url may or may not end with info.json;
        # add if not present
        if not url.endswith("info.json"):
            url = f"{ url.rstrip('/') }/info.json"
        resource_info = (
            get_info_json(url) if use_cache else get_info_json.__wrapped__(url)
        )
        self.set_hwd(resource_info.get("height"), resource_info.get("width"))
        return resource_info


monkeypatch_schema([Canvas, Resource, ResourceItem], SetHwdFromIIIF)
