# Проект Question and Answer service


## Требования

- Docker
- Docker Compose

## Запуск проекта

1. Соберите и запустите контейнеры:

```bash
  docker-compose up --build
```

2. В папке проекта запустить:

```bash
  docker-compose run backend python manage.py migrate
```

3. Проект будет доступен по адресу:
http://localhost:8000