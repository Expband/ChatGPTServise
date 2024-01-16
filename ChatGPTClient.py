import json

from IChatClient import IChat_Client
from OpenAIConnector import Open_AI_Connector


class Chat_GPT_Client(IChat_Client):
    def __init__(self):
        super().__init__()
        self.connector = Open_AI_Connector()    # init OpenAI object
        self.connection = self.connector.return_connection()    # init connection to GPT model
        self.completion = None  # init completion object
        self.response = None

    # make_request it`s a method which realise requesting to GTP model
    def make_request(self, content: str):
        try:
            self.completion = self.connection.chat.completions.create(
                model='gpt-4',
                messages=[
                    {'role': 'system',
                     'content': "Ти асистент, який допомагає з кріптовалютою."
                                "Тобі будуть задавати різного роду питання, які стосуються цієї теми."
                                "Відповідай на них як можна точніше, щоб людина мала розуміння про те, "
                                "що питає"},
                    {'role': 'user',
                     'content': f'{content}'}
                ]
            )
            self.response = self.completion.choices

            return self.response
        except Exception as ex:
            return ex

    def return_response(self):
        return self.response
