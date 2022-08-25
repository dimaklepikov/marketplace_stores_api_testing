class ResponseModel:
    def __init__(self, status: int, response: dict=None) -> None:
        self.status_code = status
        self.response = response
