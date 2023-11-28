import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dcelery.settings")

app: Celery = Celery("dcelery")
app.config_from_object("django.conf:settings", namespace="CELERY")


app.autodiscover_tasks()

app.conf.beat_schedule = {
    'task-one-every-minute': {
        'task': 'tasks.task_one',
        'schedule': crontab(minute='*'),  # Run task_one every minute
    },
    'task-two-every-hour': {
        'task': 'tasks.task_two',
        'schedule': crontab(minute=0, hour='*'),  # Run task_two every hour
    },
    # Add more tasks and their schedules using crontab as needed
}

