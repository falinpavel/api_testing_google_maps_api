import pytest # для запуска тестов
import requests # для отправки запросов
from requests import Response # для получения статус кода
from utils.checking_responses import CheckingResponses # кастомный метод для проверки статус кода
from utils.api import Google_map_api # импортируем модуль с методами HTTP

"""
This module contains tests for Google map API and extends all methods from utils/api.py module
For run tests use command: pytest -v -s
"""


class Test_google_maps_methods(): # тестирование методов Google map API, у класса нет атрибутов так как все методы статические
    def test_create_new_place(self):

        """Sending POST request"""
        print("Method POST")
        result_post: Response = Google_map_api.create_new_place()
        check_request = result_post.json()
        place_id = check_request.get("place_id")
        print("ID created place: " + place_id)
        CheckingResponses.check_status_code(result_post, 200)

        """Sending GET request"""
        print("Method GET")
        result_get: Response = Google_map_api.get_new_place(place_id)
        check_request = result_get.json()
        print(check_request)
        CheckingResponses.check_status_code(result_get, 200)

        """Sending PUT request"""
        print("Method PUT")
        result_put: Response = Google_map_api.update_new_place(place_id)
        check_request = result_put.json()
        print(check_request)
        if check_request.get("msg") == "Address successfully updated":
            assert True
            print("Test PASSED! Location successfully updated")
        else:
            assert False
            print("Test FAILED! Location doesn't updated")
        CheckingResponses.check_status_code(result_put, 200)

        """Rechecking PUT request after method PUT"""
        print("Method GET before PUT")
        result_get: Response = Google_map_api.get_new_place(place_id)
        check_request = result_get.json()
        print(check_request)
        if check_request.get("address") == "100 Lenina test PUT street, RU":
            assert True
            print("Test PASSED! Location successfully updated")
        else:
            assert False
            print("Test FAILED! Location doesn't updated")
        CheckingResponses.check_status_code(result_get, 200)

        """Sending DELETE request"""
        print("Method DELETE")
        result_delete: Response = Google_map_api.delete_new_place(place_id)
        check_request = result_delete.json()
        print(check_request)
        if check_request.get("status") == "OK":
            assert True
            print("Test PASSED! Location successfully deleted")
        else:
            assert False
            print("Test FAILED! Location doesn't deleted")
        CheckingResponses.check_status_code(result_delete, 200)

        """Rechecking GET request after method DELETE"""
        print("Method GET after DELETE")
        result_get: Response = Google_map_api.get_new_place(place_id)
        check_request = result_get.json()
        print(check_request)
        if check_request.get("msg") == "Get operation failed, looks like place_id  doesn't exists":
            assert True
            print("Test PASSED! Location successfully deleted")
        else:
            assert False
            print("Test FAILED! Location doesn't deleted")
        CheckingResponses.check_status_code(result_get, 404) # 404 - not found, location doesn't exists

