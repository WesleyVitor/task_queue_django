from celery import Celery
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store_app.settings')
django.setup()
app = Celery("store_app", broker='pyamqp://guest@localhost//')

app.autodiscover_tasks()