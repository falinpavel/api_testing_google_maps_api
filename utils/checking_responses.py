"""All methods for checking responses"""
from requests import Response


class CheckingResponses(): # класс для проверки статус кода
    """Methods for checking status code for all requests"""
    @staticmethod
    def check_status_code(response: Response, status_code: int): # метод для проверки статус кода. В аргументах передаем response (из модуля requests) и status_code (из выбранного вами метода)
        assert status_code == response.status_code # проверка статус кода
        if status_code == response.status_code: # условие. Если статус код равен статус коду из модуля requests
            print("Test status code PASSED! Fact received status code: " + str(response.status_code)) # то выводим в консоль, что тест PASSED
        else:
            print("Test status code FAILED! Fact received status code: " + str(response.status_code)) # иначе выводим в консоль, что тест FAILED
