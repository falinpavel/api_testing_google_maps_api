from utils.http_all_methods import HttpAllMethods # импортируем модуль с методами HTTP

"""All methods for testing Google map API"""

BASE_URL = "https://rahulshettyacademy.com" # для всех запросов
KEY = "?key=qaclick123" # ключ для всех запросов

"""Create calss for testing Google map API"""
class Google_map_api():

    """This method creates new location, returns ID of created location (POST)"""
    @staticmethod
    def create_new_place():
        json_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            },
            "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }
        post_resources = "/maps/api/place/add/json"
        post_url = BASE_URL + post_resources + KEY
        print("URL for POST request: " + post_url)
        result_post = HttpAllMethods.post(post_url, json_create_new_place)
        print(result_post.text)
        return result_post

    """Method for getting ID of created location (GET)"""
    @staticmethod
    def get_new_place(place_id):
        get_resources = "/maps/api/place/get/json"
        get_url = BASE_URL + get_resources + KEY + "&place_id=" + place_id
        print("URL for GET request: " + get_url)
        result_get = HttpAllMethods.get(get_url)
        print(result_get.text)
        return result_get

    """Method for updating created location (PUT)"""
    @staticmethod
    def update_new_place(place_id):
        put_resources = "/maps/api/place/update/json"
        put_url = BASE_URL + put_resources + KEY
        print("URL for PUT request: " + put_url)
        json_update_new_place = {
            "place_id": place_id,
            "address": "100 Lenina test PUT street, RU",
            "key": "qaclick123"
        }
        result_put = HttpAllMethods.put(put_url, json_update_new_place)
        print(result_put.text)
        return result_put

    """Method for deleting created location (DELETE)"""
    @staticmethod
    def delete_new_place(place_id):
        delete_resources = "/maps/api/place/delete/json"
        delete_url = BASE_URL + delete_resources + KEY
        print("URL для DELETE запроса: " + delete_url)
        json_delete_new_place = {
            "place_id": place_id
        }
        result_delete = HttpAllMethods.delete(delete_url, json_delete_new_place)
        print(result_delete.text)
        return result_delete
