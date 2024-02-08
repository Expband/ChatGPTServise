from respect_validation import Validator as validator, FormValidator as form_Validator


class Validator:
    def __init__(self):
        self._form_validator = form_Validator()
        self._error_status = bool
        self._error_message = dict
        self._error_list = list
        self.__rules = {
            'content': validator.stringType().length(1)
        }

    def validate(self, request: dict) -> dict:
        self._form_validator.validate(request=request, rules=self.__rules)
        self._error_status = self._form_validator.failed()
        print(f'Is validation failed: {self._error_status}')
        if self._error_status:
            print(f'Validation message: {self._form_validator.get_messages()}')
            self._error_message = self._form_validator.get_messages()
            print(f'Validation error: {self._form_validator.get_errors()}')
            self._error_list = self._form_validator.get_errors()
            return {'validation_status': self._error_status,
                    'validation_message': self._error_message,
                    'validation_list': self._error_list}
        return {'validation_status': self._error_status}

    def return_error_status(self):
        return self._error_status

    def return_error_message(self):
        return self._error_message

    def return_error_list(self):
        return self._error_list
