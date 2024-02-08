from openai import OpenAI
from Config.ConfigParser import *


class Open_AI_Connector:
    def __init__(self):
        self.__cfg = Config_parser()
        self.__client = None

    # initializing and returns connection
    def return_connection(self):
        try:
            print(self.__cfg.return_openai_key())
            self.__client = OpenAI(api_key=self.__cfg.return_openai_key())
            return self.__client
        except Exception as ex:
            return ex
