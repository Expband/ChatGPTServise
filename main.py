from flask import Flask
from flask_restful import Api
from GPTServise import GPT_service

app = Flask(__name__)
api = Api(app)

api.add_resource(GPT_service, '/gpt')


if __name__ == '__main__':
    app.run()
