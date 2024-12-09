# Проект api_final_yatube

## Описание проекта

Проект `api_final_yatube` представляет собой API для социальной сети Yatube, где пользователи могут публиковать, редактировать и удалять посты, комментировать и управлять комментариями, просмаривать сообщества, подписываться на других пользователей, получать, обновлять и проверять токены.

## Автор

Авторы проекта: Яндекс Практикум, Олег Ритум. 

Год разаботки: 2024.

## Развертывание проекта

#### Шаг 1: Клонирование репозитория

```bash
git clone git@github.com:<username>/api_final_yatube.git
```

```bash
cd api_final_yatube
```

#### Шаг 2: Создание и активация виртуального окружения

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

#### Шаг 3: Установка зависимостей

```bash
python3 -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

#### Шаг 4: Применение миграций

```bash
python manage.py migrate
```

#### Шаг 5: Запуск сервера разработки

```bash
python manage.py runserver
```

## Примеры запросов и ответов:

### Получение списка постов

**Запрос:**

```http
GET .../api/v1/posts/
```

**Ответ:**

```json
[
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
]
```

#### Создание поста

**Запрос:**

```http
POST .../api/v1/posts/

{
  "text": "string",
  "image": "string",
  "group": 0
}

```

**Ответ:**

```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

### Получение списка сообществ

**Запрос:**

```http
GET .../api/v1/groups/
```

**Ответ:**

```json
[
  {
    "id": 0,
    "title": "string",
    "slug": "^-$",
    "description": "string"
  }
]
```

### Возвращает все подписки пользователя, сделавшего запрос.

**Запрос:**

```http
GET .../api/v1/follow/


```

**Ответ:**

```json
[
  {
    "user": "string",
    "following": "string"
  }
]
```


### Получение JWT-токена.

**Запрос:**

```http
POST .../api/v1/jwt/create/

{
  "username": "string",
  "password": "string"
}
```

**Ответ:**

```json
{
  "refresh": "string",
  "access": "string"
}
```
