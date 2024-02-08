from abc import ABC, abstractmethod


class IResponser(ABC):
    def __init__(self):
        self.__response_body: dict = {}

    @abstractmethod
    def send_response(self, status_code: int, response_body: dict):
        pass
