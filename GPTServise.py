from IService import IService
from flask import request, make_response, jsonify
from flask_restful import Resource
from ChatGPTClient import Chat_GPT_Client
from Validator import Validator


class GPT_service(Resource, IService):
    def __init__(self):
        super().__init__()
        self.__validator = Validator()
        self.__gpt_client = Chat_GPT_Client()
        self.__raw_request = None

    def get(self):
        pass

    def post(self):
        self.__raw_request = request.get_json()
        if self.__validator.validate(request=self.__raw_request):
            print(self.__raw_request['content'])
            self.__gpt_client.make_request(content=self.__raw_request['content'])
            response_payload = self.__gpt_client.return_response()
            return make_response(jsonify(response_payload), 200)
