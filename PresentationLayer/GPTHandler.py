from BussinesLogicLayer.IService import IService
from flask import request, make_response, jsonify
from flask_restful import Resource
from BussinesLogicLayer.ChatGPTClient import Chat_GPT_Client
from PresentationLayer.Validator import Validator


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
        if not self.__validator.validate(request=self.__raw_request)['validation_status']:
            self.__response = self.__gpt_client.make_request(content=self.__raw_request['content'])
            print(self.__response)
            return make_response(jsonify({'choices': {'message': self.__response[0].message.content,
                                                            'finish_reason': self.__response[0].finish_reason,
                                                            'index': self.__response[0].index}}), 200)
        else:
            return make_response(jsonify({'error': {
                f'content': f'{self.__validator.return_error_message()['content']}'
            }}), 400)
