#!/bin/bash

python "/app/manage.py" migrate

python "/app/manage.py" collectstatic --noinput

gunicorn -c "./deploy/gunicorn.conf.py" src.wsgi:application