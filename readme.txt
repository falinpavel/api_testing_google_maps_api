Документация Google Map API

Метод POST
Запрос:
Base URL: https://rahulshettyacademy.com
Resource: /maps/api/place/add/json
Параметр для всех запросов: key =qaclick123
Body:
{
"location": {
"lat": -38.383494,
"lng": 33.427362
}, "accuracy": 50,
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

Ответ:
Статус: 200. Запрос прошел успешно
{
    "status": "OK",
    "place_id": "dea036e58d6773b3f8bfb256249a1593",
    "scope": "APP",
    "reference": "1f71a23b1374071eecbb70eed1054cf91f71a23b1374071eecbb70eed1054cf9",
    "id": "1f71a23b1374071eecbb70eed1054cf9"
}


Метод GET
Base URL: https://rahulshettyacademy.com
Resource: /maps/api/place/get/json
Параметр для запросов: key =qaclick123, place_id

Ответ:
Статус: 200. Запрос прошел успешно
{
    "location": {
        "latitude": "-38.383494",
        "longitude": "33.427362"
    },
    "accuracy": "50",
    "name": "Frontline house",
    "phone_number": "(+91) 983 893 3937",
    "address": "29, side layout, cohen 09",
    "types": "shoe park,shop",
    "website": "http://google.com",
    "language": "French-IN"
}

Статус: 404. Ошибка, локация с таким place_id отсутствует
{
    "msg": "Get operation failed, looks like place_id  doesn't exists"
}

Метод PUT
Запрос:
Base URL: https://rahulshettyacademy.com
Resource: /maps/api/place/update/json
Параметр для запросов: key =qaclick123
Body:
{
"place_id":"c104d917f4b60e2c9a5feda6c9cbf279",
 "address":"100 Lenina street, RU",
"key":"qaclick123"
}

Ответ:
Статус: 200. Запрос прошел успешно
{
    "msg": "Address successfully updated"
}

Статус: 404. Ошибка, локация с таким place_id отсутствует
{
    "msg": "Update address operation failed, looks like the data doesn't exists"
}


Метод DELETE
Запрос:
Base URL: https://rahulshettyacademy.com
Resource: /maps/api/place/delete/json
Параметр для запросов: key =qaclick123
Body:
{
"place_id":"928b51f64aed18713b0d164d9be8d67f"
}

Ответ:
Статус: 200. Запрос прошел успешно
{
    "status": "OK"
}

Статус: 404. Ошибка, локация с таким place_id отсутствует
{
    "msg": "Delete operation failed, looks like the data doesn't exists"
}