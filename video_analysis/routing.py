# video_analysis/routing.py

from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/video/<str:video_id>/', consumers.VideoConsumer.as_asgi()),
]
