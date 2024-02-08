from abc import ABC, abstractmethod


class IChat_Client(ABC):
    def __init__(self):
        self.content = str
        self.response = None

    @abstractmethod
    def make_request(self, content: str):
        pass

    @abstractmethod
    def return_response(self):
        pass
