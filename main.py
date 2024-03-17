from flask import Flask
from flask_restful import Api
from PresentationLayer.GPTHandler import GPT_service
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)

api.add_resource(GPT_service, '/gpt')


if __name__ == '__main__':
    app.run(port=5002)
