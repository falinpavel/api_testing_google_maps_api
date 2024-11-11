import json

import pytest  # для запуска тестов
import requests  # для отправки запросов
from requests import Response  # для получения статус кода
from utils.checking_responses import CheckingResponses  # кастомный метод для проверки статус кода
from utils.api import Google_map_api  # импортируем модуль с методами HTTP

"""
This module contains tests for Google map API and extends all methods from utils/api.py module
For run tests use command: pytest -v -s
"""


class Test_google_maps_methods():  # тестирование методов Google map API, у класса нет атрибутов так как все методы статические
    def test_create_new_place(self):
        """Sending POST request"""
        print("Method POST")
        result_post: Response = Google_map_api.create_new_place()
        check_request = result_post.json()
        place_id = check_request.get("place_id")
        print("ID created place: " + place_id)
        CheckingResponses.check_status_code(result_post, 200)
        CheckingResponses.check_required_fields(result_post,
                                                ["status", "place_id", "scope", "reference", "id"])
        CheckingResponses.check_field_value(result_post,"status", "OK")
        CheckingResponses.check_field_value(result_post,"scope", "APP")

        """
        # token = json.loads(result_post.text)
        # print(list(token)) # получаем список полей в response
        """

        """Sending GET request"""
        print("Method GET")
        result_get: Response = Google_map_api.get_new_place(place_id)
        check_request = result_get.json()
        print(check_request)
        CheckingResponses.check_status_code(result_get, 200)
        CheckingResponses.check_required_fields(result_get,
                                                ["location", "accuracy", "name", "phone_number", "address", "types",
                                                 "website", "language"])
        CheckingResponses.check_field_value(result_get,"accuracy", "50")
        CheckingResponses.check_field_value(result_get,"name", "Frontline house")
        CheckingResponses.check_field_value(result_get,"phone_number", "(+91) 983 893 3937")
        CheckingResponses.check_field_value(result_get,"address", "29, side layout, cohen 09")
        CheckingResponses.check_field_value(result_get,"types", "shoe park,shop")
        CheckingResponses.check_field_value(result_get,"website", "http://google.com")
        CheckingResponses.check_field_value(result_get,"language", "French-IN")

        """Sending PUT request"""
        print("Method PUT")
        result_put: Response = Google_map_api.update_new_place(place_id)
        check_request = result_put.json()
        print(check_request)
        CheckingResponses.check_status_code(result_put, 200)
        CheckingResponses.check_required_fields(result_put,
                                                ["msg"])
        CheckingResponses.check_field_value(result_put,"msg", "Address successfully updated")

        """Rechecking GET request after method PUT"""
        print("Method GET before PUT")
        result_get: Response = Google_map_api.get_new_place(place_id)
        check_request = result_get.json()
        print(check_request)
        CheckingResponses.check_status_code(result_get, 200)
        CheckingResponses.check_required_fields(result_get,
                                                ["location", "accuracy", "name", "phone_number", "address", "types",
                                                 "website", "language"])
        CheckingResponses.check_field_value(result_get,"address", "100 Lenina test PUT street, RU")

        """Sending DELETE request"""
        print("Method DELETE")
        result_delete: Response = Google_map_api.delete_new_place(place_id)
        check_request = result_delete.json()
        print(check_request)
        CheckingResponses.check_status_code(result_delete, 200)
        CheckingResponses.check_required_fields(result_delete,
                                                ["status"])
        CheckingResponses.check_field_value(result_delete,"status", "OK")

        """Rechecking GET request after method DELETE"""
        print("Method GET after DELETE")
        result_get: Response = Google_map_api.get_new_place(place_id)
        check_request = result_get.json()
        print(check_request)
        CheckingResponses.check_status_code(result_get, 404)  # 404 - not found, location doesn't exists
        CheckingResponses.check_required_fields(result_get,
                                                ["msg"])
        CheckingResponses.check_field_value(result_get,
                                            "msg", "Get operation failed, looks like place_id  doesn't exists")

        print("Test create new place completed (POST -> GET -> PUT -> GET -> DELETE -> GET)")
