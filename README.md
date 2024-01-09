# Образовательная платформа

Сайт для ДВГУПС

## Технологический стек
- Python 3.10
- Django 4.2.7
- PostgreSQL
- Docker
- Docker-compose


# Инструкция по развертыванию

Создать .env из .env.example

#### Параметры приложения
|       Ключ        | Значение                         | Примечания                         |
|-------------------|----------------------------------|------------------------------------|
|`DEBUG`| Настройка режима запуска проекта | `*`                                |
|`TIME_ZONE`| Часовой пояс                     | `*`                                |
|`DB_ENGINE`| Движок для бд                    | `*`                                |
|`DB_NAME`| Имя дб                           | `*`                                |
|`DB_USER`| Пользователь бд                  | `*`                                |
|`DB_PASSWORD`| Пароль к дб                      | `*`                                |
|`DB_HOST`| Хост дб                          | `*`                                |
|`DB_PORT`| Порт дб                          | `*`                                |
|`REDIS_HOST`| Хост брокера redis               | `*`                                |
|`REDIS_PORT`| Порт брокера redis               | *                                  |
|`SESSION_ENGINE`| Движок для сессии                | *                                  |
|`DOMAIN`| Домен сайта                      | Исп. для csrf_trusted в setting.py |

### Запуск через докер 
В корне проекта (где файлы докера) 
```shell
docker-compose up --build
```
Затем создать супер-пользователя джанго
```shell
docker ps
```
```shell
docker exec -it <id_контейнера_web> bash
```
```shell
python manage.py createsuperuser
```

### Запуск вручную
1. В PgAdmin4 создать базу данных.
2. Выполнить миграции
```shell
python manage.py migrate
```
3. Запустить проект 
```shell
python manage.py runserver
```
4. Создать супер-пользователя джанго
```shell
python manage.py createsuperuser
```

### При изменении кода запускать команду

```shell
ctrl+c
```

```shell
docker-compose down
```
```shell
docker-compose up --build
```