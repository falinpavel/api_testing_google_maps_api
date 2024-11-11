from utils.logger import Logger

import allure
import requests

"""
This module contains all custom HTTP methods: 
GET, 
POST, 
PUT, 
DELETE
"""


class HttpAllMethods:
    headers = {
        'Content-Type': 'application/json'
    }
    cookies = ""

    @staticmethod  # статический метод. Проставляем, нужно обращаться к нему без создания экземпляра
    def get(url):  # не передаем self в качестве аргумента, так как делаем наши методы статическими
        with allure.step("GET request: " + url):
            Logger.add_request(url, "GET")
            result = requests.get(url, headers=HttpAllMethods.headers, cookies=HttpAllMethods.cookies)
            Logger.add_response(result)
            return result

    @staticmethod
    def post(url, body):  # обязательно передаем body
        with allure.step("POST request: " + url):
            Logger.add_request(url, "POST")
            result = requests.post(url, json=body, headers=HttpAllMethods.headers, cookies=HttpAllMethods.cookies)
            Logger.add_response(result)
            return result

    @staticmethod
    def put(url, body):  # обязательно передаем body
        with allure.step("PUT request: " + url):
            Logger.add_request(url, "PUT")
            result = requests.put(url, json=body, headers=HttpAllMethods.headers, cookies=HttpAllMethods.cookies)
            Logger.add_response(result)
            return result

    @staticmethod
    def delete(url, body):
        with allure.step("DELETE request: " + url):
            Logger.add_request(url, "DELETE")
            result = requests.delete(url, json=body, headers=HttpAllMethods.headers, cookies=HttpAllMethods.cookies)
            Logger.add_response(result)
            return result

