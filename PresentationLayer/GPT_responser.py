from PresentationLayer.IResponser import IResponser
from flask import make_response, jsonify


class GPT_responser(IResponser):
    def send_response(self, status_code: int, response_body: dict):
        if status_code == 200:
            return make_response(jsonify({'chooses': {'message': response_body['message'],
                                                      'finish_reason': response_body['finish_reason'],
                                                      'index': response_body['index']}}), status_code)
        if status_code == 400:
            return make_response(jsonify({'error': {
                'content': f'{response_body['content']}'
            }}), status_code)
