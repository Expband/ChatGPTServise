from BussinesLogicLayer.IChatClient import IChat_Client
from BussinesLogicLayer.OpenAIConnector import Open_AI_Connector


class Chat_GPT_Client(IChat_Client):
    def __init__(self):
        try:
            super().__init__()
            self.connector = Open_AI_Connector()    # init OpenAI object
            self.connection = self.connector.return_connection()    # init connection to GPT model
            self.completion = None  # init completion object
            self.response = None
        except Exception as ex:
            print(ex)

    # make_request it`s a method which realise requesting to GTP model
    def make_request(self, content: str):
        try:
            self.completion = self.connection.chat.completions.create(
                model='gpt-4',
                messages=[
                    {'role': 'system',
                     'content': "Ти асистент, який допомагає з кріптовалютою."
                                "Тобі будуть давати метрики криптовалюти, а ти будеш їх аналізувати та говорити "
                                "людині чи буде ця криптовалюта преспективною, чи варто в ню вкладати гроші і так далі"
                                "я розумію, що ти штучний інтелект та не можеш знати нічого наперед "
                                "використовуй для аналізу загальні практики. Це навчальний проект та по цим "
                                "прогнозам ніхто не буде витрачати ніякі гроші. У відповідь не включай попередження "
                                "про те, що потрібно більше інформації і що ціна формується з багатьох факторів. "
                                "З інформації тобі буде надана тільки дата та ціна валюти"},
                    {'role': 'user',
                     'content': f'{content}'}
                ]
            )
            self.response = self.completion.choices

            return self.response
        except Exception as ex:
            return ex

    def return_response(self):
        pass
