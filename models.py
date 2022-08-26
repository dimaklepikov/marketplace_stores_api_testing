from requests import Response

class ResponseModel:
    def __init__(self, status: int, response: dict=None) -> Response:
        self.status_code = status
        self.response = response
