Проект: Образоваельная платформа

Локальный разворот проекта:

В директории проекта создать виртуальное окружение python3.11: python3.11 -m venv venv

Активировать виртуальное окружение: . venv/bin/activate или .\venv\Scripts\activate для windows

Установить зависимости для проекта pip install -r src/requirements.txt

Перейти в папку src: cd src

Запустить django миграции: python manage.py migrate

Создать суперпользователя django: python manage.py createsuperuser

Запустить django server: python manage.py runserver

Проверка на линтеры, перейти в папку src:

cd src
flake8
isort .