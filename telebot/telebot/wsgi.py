"""
WSGI config for telebot project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'telebot.settings')

application = get_wsgi_application()


import psycopg2

try:
    # пытаемся подключиться к базе данных
    conn = psycopg2.connect(dbname='test', user='postgres', password='secret', host='host')
except:
    # в случае сбоя подключения будет выведено сообщение в STDOUT
    print('Can`t establish connection to database')
