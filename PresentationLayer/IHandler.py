from abc import ABC


class IService(ABC):
    def __init__(self):
        self.__validator = None
        self.__gpt_client = None
        self.__raw_request = None

    def get(self):
        pass

    def post(self):
        pass
