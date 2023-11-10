from __future__ import absolute_import

import os

from celery import Celery
from celery.schedules import crontab

from django.conf import settings

os.environ.setdefault(key='DJANGO_SETTINGS_MODULE', value='agrotool.settings')

app = Celery('agrotool')

app.config_from_object('django.conf:settings')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
