import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
if "DJANGO_SETTINGS_MODULE" not in os.environ:
    raise Exception(
        "DJANGO_SETTINGS_MODULE must be set in the environment before running celery."
    )
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quant_trading.settings')

app = Celery('quant_trading')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


# @app.task(bind=True, ignore_result=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')