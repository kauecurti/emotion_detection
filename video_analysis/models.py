# video_analysis/models.py
from django.db import models

class VideoProcessingStatus(models.Model):
    video = models.FileField(upload_to='videos/')
    task_id = models.CharField(max_length=255)
    status = models.CharField(max_length=50, default='PENDING')
