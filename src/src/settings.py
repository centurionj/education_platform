import os
from pathlib import Path

from django.core.management.utils import get_random_secret_key
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = get_random_secret_key()

DEBUG = os.getenv('DEBUG'),

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = [os.getenv('DOMAIN'), 'http://localhost']


INSTALLED_APPS = [
    'jazzmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'ckeditor',
    'ckeditor_uploader',
    'nested_inline',
    'django_cleanup',

    'main',
    'news',
    'setups',
    'common',
    'courses',
    'users',
    'favourites',
    'lectures',
    'testing',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'src.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'src.wsgi.application'

# Database

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization

LANGUAGE_CODE = 'ru'

TIME_ZONE = os.getenv('TIME_ZONE')

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js'
CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_CONFIGS = {
    'default': {
        'autoGrow_bottomSpace': 10,
        'toolbar': 'full',
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# redis

REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')

# celery

CELERY_BROKER_URL = 'redis://{}:{}/0'.format(os.getenv('REDIS_HOST'), os.getenv('REDIS_PORT'))
CELERY_RESULT_BACKEND = 'redis://{}:{}/0'.format(os.getenv('REDIS_HOST'), os.getenv('REDIS_PORT'))
CELERY_IMPORTS = ('customers.tasks', )
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE

# Users

AUTH_USER_MODEL = 'users.User'
LOGIN_REDIRECT_URL = 'dashboard_redirect'

# Session

SESSION_ENGINE = os.getenv('SESSION_ENGINE')
SESSION_COOKIE_NAME = 'my_session'
SESSION_COOKIE_AGE = 30 * 24 * 3600  # для админки
SESSION_EXPIRE_SECONDS = 3600  # для обычных пользователей
SESSION_COOKIE_SECURE = False  # для использования HTTPS (True)
SESSION_COOKIE_HTTPONLY = True  # закрыл доступ к cookie через JS
SESSION_SAVE_EVERY_REQUEST = True  # для сохранения сессии при перемещении на сайте
SESSION_COOKIE_SAMESITE = 'Lax'

# PDF

X_FRAME_OPTIONS = 'SAMEORIGIN'

# admin

JAZZMIN_SETTINGS  = {
    "site_title": "ДВГУПС",
    "site_header": "ДВГУПС",
    "site_brand": "ДВГУПС",
}
