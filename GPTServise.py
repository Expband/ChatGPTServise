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
        self.__response = None

    def get(self):
        pass

    def post(self):
        self.__raw_request = request.get_json()
        if self.__validator.validate(request=self.__raw_request):
            self.__response = self.__gpt_client.make_request(content=self.__raw_request['content'])
            return jsonify({'response_object': {'message': self.__response[0].message.content,
                                                'finish_reason': self.__response[0].finish_reason,
                                                'index': self.__response[0].index}})
