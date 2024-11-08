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
