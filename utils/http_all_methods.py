import requests

"""Список HTTP методов для запросов"""
"""GET, POST, PUT, PATCH, DELETE"""

class HttpAllMethods:
    headers = {
        'Content-Type': 'application/json'
    }
    cookies = ""
    @staticmethod  # статический метод. Проставляем, нужно обращаться к нему без создания экземпляра
    def get(url):  # не передаем self в качестве аргумента, так как делаем наши методы статическими
        result = requests.get(url, headers=HttpAllMethods.headers, cookies=HttpAllMethods.cookies)
        return result
    @staticmethod
    def post(url, body): # обязательно передаем body
        result = requests.post(url, json=body, headers=HttpAllMethods.headers, cookies=HttpAllMethods.cookies)
        return result
    @staticmethod
    def put(url, body): # обязательно передаем body
        result = requests.put(url, json=body, headers=HttpAllMethods.headers, cookies=HttpAllMethods.cookies)
        return result
    @staticmethod
    def delete(url):
        result = requests.delete(url, headers=HttpAllMethods.headers, cookies=HttpAllMethods.cookies)
        return result
    @staticmethod
    def patch(url, body): # обязательно передаем body
        result = requests.patch(url, json=body, headers=HttpAllMethods.headers, cookies=HttpAllMethods.cookies)
        return result
