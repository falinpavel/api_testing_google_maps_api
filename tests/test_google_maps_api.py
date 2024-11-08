import pytest
import requests
from requests import Response

from utils.api import Google_map_api

"""Создание, изменение и удаление локации"""


class Test_google_maps_methods():
    def test_create_new_place(self):
        """Отправка POST запроса"""
        print("Method POST")
        result_post: Response = Google_map_api.create_new_place()
        check_request = result_post.json()
        place_id = check_request.get("place_id")
        print("ID для новой созданной локации: " + place_id)

        """Отправка GET запроса"""
        print("Method GET")
        result_get: Response = Google_map_api.get_new_place(place_id)
        check_request = result_get.json()
        print(check_request)

        """Отправка PUT запроса"""
        print("Method PUT")
        result_put: Response = Google_map_api.update_new_place(place_id)
        check_request = result_put.json()
        print(check_request)
        if check_request.get("msg") == "Address successfully updated":
            assert True
            print("Тест PASSED! Локация успешно изменена")
        else:
            assert False
            print("Тест FAILED! Локация не изменена")

        """Проверка изменения локации методом GET"""
        print("Method GET")
        result_get: Response = Google_map_api.get_new_place(place_id)
        check_request = result_get.json()
        print(check_request)
        if check_request.get("address") == "100 Lenina test PUT street, RU":
            assert True
            print("Тест PASSED! Локация успешно изменена")
        else:
            assert False
            print("Тест FAILED! Локация не изменена")

        """Отправка DELETE запроса"""

