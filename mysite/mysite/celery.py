from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
app = Celery('mysite')
app.conf.broker_url = 'redis://redis:6379/0'
app.autodiscover_tasks()