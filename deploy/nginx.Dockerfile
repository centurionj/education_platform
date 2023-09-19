FROM nginx:stable-alpine

ENV DOLLAR $

COPY ./django-default.conf.template /etc/nginx/templates/default.conf.template
