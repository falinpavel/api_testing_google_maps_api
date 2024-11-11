# Документация Google Map API
## Метод POST
### _Запрос:_
* _Base URL: https://rahulshettyacademy.com_
* _Resource: /maps/api/place/add/json_
* _Параметр для всех запросов: key =qaclick123_

### _Body:_
```json
{
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
```
### _Ответ (Статус: 200. Запрос прошел успешно):_
```json
{
    "status": "OK",
    "place_id": "dea036e58d6773b3f8bfb256249a1593",
    "scope": "APP",
    "reference": "1f71a23b1374071eecbb70eed1054cf91f71a23b1374071eecbb70eed1054cf9",
    "id": "1f71a23b1374071eecbb70eed1054cf9"
}
```

## Метод GET
* _Base URL: https://rahulshettyacademy.com_
* _Resource: /maps/api/place/get/json_
* _Параметр для запросов: key =qaclick123, place_id_

### _Ответ (Статус: 200. Запрос прошел успешно):_
```json
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
```

### _Ответ (Статус: 404. Ошибка, локация с таким place_id отсутствует):_
```json
{
    "msg": "Get operation failed, looks like place_id  doesn't exists"
}
```

## Метод PUT
### _Запрос:_
* _Base URL: https://rahulshettyacademy.com_
* _Resource: /maps/api/place/update/json_
* _Параметр для запросов: key =qaclick123_
### _Body:_
```json
{
    "place_id": "c104d917f4b60e2c9a5feda6c9cbf279",
    "address": "100 Lenina street, RU",
    "key": "qaclick123"
}
```
### _Ответ (Статус: 200. Запрос прошел успешно):_
```json
{
    "msg": "Address successfully updated"
}
```
### _Ответ (Статус: 404. Ошибка, локация с таким place_id отсутствует):_
```json
{
    "msg": "Update address operation failed, looks like the data doesn't exists"
}
```

## Метод DELETE
### _Запрос:_
* _Base URL: https://rahulshettyacademy.com_
* _Resource: /maps/api/place/delete/json_
* _Параметр для запросов: key =qaclick123_
### _Body:_
```json
{
    "place_id": "928b51f64aed18713b0d164d9be8d67f"
}
```
### _Ответ (Статус: 200. Запрос прошел успешно):_
```json
{
    "status": "OK"
}
```
### _Ответ (Статус: 404. Ошибка, локация с таким place_id отсутствует):_
```json
{
    "msg": "Delete operation failed, looks like the data doesn't exists"
}
```