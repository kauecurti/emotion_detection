# video_analysis/tasks.py
from celery import shared_task
from .video_processing import analyze_video
from django_celery_results.models import TaskResult
import json
import cv2


@shared_task(bind=True)
def process_video_task(self, video_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cap.release()

    result = analyze_video(video_path, face_cascade, self, total_frames)
    emotion_counts = {
        'happy': sum(1 for _, e, _ in result if e == 'happy'),
        'sad': sum(1 for _, e, _ in result if e == 'sad'),
        'neutral': sum(1 for _, e, _ in result if e == 'neutral'),
        'angry': sum(1 for _, e, _ in result if e == 'angry'),
        'surprise': sum(1 for _, e, _ in result if e == 'surprise'),
        'fear': sum(1 for _, e, _ in result if e == 'fear')
    }
    # Salvar o resultado no TaskResult
    TaskResult.objects.create(
        task_id=self.request.id,
        status='SUCCESS',
        result=json.dumps(emotion_counts)
    )
    return emotion_counts
