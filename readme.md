# Google Maps API Automation Tests

Этот проект содержит автотесты для тестирования API [Google Maps](https://rahulshettyacademy.com). Тесты автоматизируют основные операции с ресурсами API, включая создание, получение, обновление и удаление локаций.

## 📋 Описание API

| HTTP Метод   | Операция                                   | Ресурс                                   | Примечания                             |
|--------------|--------------------------------------------|------------------------------------------|----------------------------------------|
| **POST**     | Добавить новую локацию                     | `/maps/api/place/add/json`               | Создает новую локацию с указанными параметрами |
| **GET**      | Получить информацию о локации              | `/maps/api/place/get/json`               | Возвращает данные о локации по `place_id` |
| **PUT**      | Обновить адрес существующей локации        | `/maps/api/place/update/json`            | Обновляет адрес по указанному `place_id` |
| **DELETE**   | Удалить существующую локацию               | `/maps/api/place/delete/json`            | Удаляет локацию по указанному `place_id` |

---

## 🛠️ Используемые технологии

- **Язык программирования:** Python
- **Фреймворк для тестирования:** pytest
- **HTTP-клиент:** requests
- **Менеджер зависимостей:** pip

---

## 📂 Структура проекта

```plaintext
├── api/                       # Реализация HTTP-запросов (POST, GET, PUT, DELETE)
├── tests/                     # Тестовые сценарии
├── utils/                     # Вспомогательные функции (например, генерация данных)
├── pytest.ini                 # Конфигурация pytest
├── requirements.txt           # Список зависимостей
└── README.md                  # Описание проекта
```
## 🧪 Покрытие тестов

| HTTP Метод | Операция                        | Статус    | Количество тестов | Примечания                        |
|------------|---------------------------------|-----------|-------------------|-----------------------------------|
| POST       | Добавить новую локацию          | ✅        | 5                 | Проверены позитивные и негативные сценарии |
| GET        | Получить данные о локации       | ✅        | 4                 | Покрыты успешные и ошибочные ответы |
| PUT        | Обновить адрес локации          | ✅        | 3                 | Проверено успешное обновление и отсутствие данных |
| DELETE     | Удалить локацию                 | ✅        | 3                 | Успешное удаление и сценарии ошибок |

---

## 🚀 Как запустить тесты

### Шаг 1. Установите зависимости
Убедитесь, что Python версии 3.8+ установлен на вашем компьютере.

```bash
pip install -r requirements.txt
```

### Шаг 2. Настройте переменные окружения
Создайте файл .env в корне проекта и укажите параметры:

```bash
BASE_URL=https://rahulshettyacademy.com
API_KEY=qaclick123
```
### Шаг 3. Запустите тесты

```bash
pytest --html=report.html --self-contained-html (OR pytest -s -v)
```

## 📑 Примеры тестов

### 1. POST — Добавить новую локацию

```python
def test_create_place(api_client):
    body = {
        "location": {"lat": -38.383494, "lng": 33.427362},
        "accuracy": 50,
        "name": "Frontline house",
        "phone_number": "(+91) 983 893 3937",
        "address": "29, side layout, cohen 09",
        "types": ["shoe park", "shop"],
        "website": "http://google.com",
        "language": "French-IN"
    }
    response = api_client.post("/maps/api/place/add/json", json=body, params={"key": "qaclick123"})
    assert response.status_code == 200
    assert response.json()["status"] == "OK"
```

### 2. GET — Получить данные о локации

```python
def test_get_place(api_client, place_id):
    response = api_client.get("/maps/api/place/get/json", params={"key": "qaclick123", "place_id": place_id})
    assert response.status_code == 200
    assert response.json()["name"] == "Frontline house"
```

## 🤝 Контрибьютинг
Если вы хотите внести свой вклад в проект:

1. Форкните репозиторий.
2. Создайте ветку с вашей задачей (git checkout -b feature/new-feature).
3. Внесите изменения и создайте Pull Request.