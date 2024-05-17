# emotion_detection/celery.py
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'emotion_detection.settings')

app = Celery('emotion_detection')

# Configuração do Celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# Definindo o pool como 'solo' diretamente no Celery
app.conf.update(
    broker_url='redis://:foobared@localhost:6379/0',
    result_backend='redis://:foobared@localhost:6379/0',
    worker_concurrency=1,  # Limitar a concorrência
    worker_pool='solo',  # Usar 'solo' para evitar fork
)

app.autodiscover_tasks()
