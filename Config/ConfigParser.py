import configparser
import os


class Config_parser:
    def __init__(self):
        try:
            self.__path = os.path.join(os.path.dirname(__file__), 'config.ini')
            self.__cfg = configparser.ConfigParser()
            self.__cfg.read(self.__path)
            self.__OPEN_AI_API_KEY = self.__cfg['openai']['API_KEY']
        except Exception as ex:
            print(str(ex))

    def return_openai_key(self):
        try:
            return self.__OPEN_AI_API_KEY
        except Exception as ex:
            return ex
