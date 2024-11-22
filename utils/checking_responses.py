"""All methods for checking responses"""
import json

from requests import Response


class CheckingResponses(): # класс для проверки ответа
    """Methods for checking status code for all requests"""
    @staticmethod
    def check_status_code(response: Response, status_code: int): # метод для проверки статус кода. В аргументах передаем response (из модуля requests) и status_code (из выбранного вами метода)
        assert status_code == response.status_code # проверка статус кода
        if status_code == response.status_code: # условие. Если статус код равен статус коду из модуля requests
            print("Test status code PASSED! Fact received status code: " + str(response.status_code)) # то выводим в консоль, что тест PASSED
        else:
            print("Test status code FAILED! Fact received status code: " + str(response.status_code)) # иначе выводим в консоль, что тест FAILED

    """Check required fields in response"""
    @staticmethod
    def check_required_fields(response: Response, expected_fields):
        fields = json.loads(response.text)
        assert list(fields) == expected_fields
        if list(fields) == expected_fields:
            print("Test required fields PASSED! Fact received required fields: " + str(expected_fields))
        else:
            print("Test required fields FAILED! Fact received required fields: " + str(expected_fields))

    """Check value in response fields"""
    @staticmethod
    def check_field_value(response: Response, exp_field_name, exp_field_value):
        check_fields = response.json()
        check_value = check_fields.get(exp_field_name)
        assert check_value == exp_field_value
        if check_value == exp_field_value:
            print("Test field value PASSED! Fact received field value: " + str(exp_field_value))
        else:
            print("Test field value FAILED! Fact received field value: " + str(exp_field_value))

    """Check specific word in response"""
    @staticmethod
    def check_word_in_response(response: Response, exp_field_name, exp_word):
        check_fields = response.json()
        check_value = check_fields.get(exp_field_name)
        assert exp_word in check_value
        if exp_word in check_value:
            print("Test word in response PASSED! Fact received word in response: " + str(exp_word))
        else:
            print("Test word in response FAILED! Fact received word in response: " + str(exp_word))