# ProtestTask

## Описание

Это серверное приложение, которое предоставляет API для управления пользователями и заказами.

## Требования

- Python 3.10 или выше
- PostgreSQL
- Docker

## Инструкции по запуску

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/IlyaKorol/protettask.git
    cd protettask
    ```

2. Создайте и активируйте виртуальное окружение:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # для MacOS/Linux
    venv\Scripts\activate  # для Windows
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

4. Запустите Docker:
    ```bash
    docker-compose up --build
    ```

    Это создаст и запустит два контейнера:
    - **web**: ваше Django-приложение
    - **db**: база данных PostgreSQL

5. Выполните миграции:
    ```bash
    docker-compose exec web python manage.py migrate
    ```

6. Приложение будет доступно по адресу: [http://localhost:8000](http://localhost:8000)

## API

### Пользователи

- `GET /api/users/`: Получить список пользователей
- `POST /api/users/`: Создать нового пользователя
- `PUT /api/users/{id}/`: Обновить информацию о пользователе

### Заказы

- `GET /api/orders/`: Получить список заказов
- `POST /api/orders/`: Создать новый заказ
- `PUT /api/orders/{id}/`: Обновить информацию о заказе
