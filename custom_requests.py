import requests
from requests import Response

class Client:
    @staticmethod
    def custom_request(method: str, url: str, **kwargs) -> Response:
        """
        **kwargs:
        params
        json
        headers
        """
        return requests.request(method, url, **kwargs)
