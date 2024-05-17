from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_video, name='upload_video'),
    path('progress/<task_id>/', views.task_progress, name='task_progress'),
    path('results/<int:video_id>/', views.results, name='results'),
]
