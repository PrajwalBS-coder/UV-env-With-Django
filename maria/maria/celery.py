from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'maria.settings')

app = Celery('maria')

app.config_from_object(settings, namespace='CELERY')

# Celery Beat Settings
app.conf.beat_schedule={}


app.autodiscover_tasks()
@app.task(bind= True)
def debug_task(self):
    print(f"CELERY DEBUG TASK FUNCTION:{self.request!r}")