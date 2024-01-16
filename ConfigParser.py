import configparser


class Config_parser:
    def __init__(self):
        self.__cfg = configparser.ConfigParser()
        self.__cfg.read('config.ini')
        self.__OPEN_AI_API_KEY = self.__cfg['openai']['API_KEY']

    def return_openai_key(self):
        return self.__OPEN_AI_API_KEY
