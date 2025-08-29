# Проект Question and Answer service


## Требования

- Docker
- Docker Compose

## Запуск проекта

1. Создать .env и добавить переменные окружение из примера [.env.example](.env.example)


2. Соберите и запустите контейнеры:

```bash
  docker-compose up --build
```

3. В папке проекта запустить:

```bash
  docker-compose run backend python manage.py migrate
```

4. Проект будет доступен по адресу:
http://localhost:8000