import json

from django.shortcuts import render, redirect, get_object_or_404
from django_celery_results.models import TaskResult

from .models import VideoProcessingStatus
from .tasks import process_video_task
from django.http import JsonResponse
from celery.result import AsyncResult

def index(request):
    return render(request, 'video_analysis/index.html')

def upload_video(request):
    if request.method == 'POST':
        video = request.FILES['video']
        video_status = VideoProcessingStatus.objects.create(video=video)
        task = process_video_task.delay(video_status.video.path)
        video_status.task_id = task.id
        video_status.save()
        return JsonResponse({'task_id': task.id})
    return render(request, 'video_analysis/upload.html')

def progress(request, video_id):
    video = VideoProcessingStatus.objects.get(id=video_id)
    if video.status == 'SUCCESS':
        return redirect('results', video_id=video.id)
    return JsonResponse({'status': video.status})


def results(request, video_id):
    video_status = get_object_or_404(VideoProcessingStatus, id=video_id)

    if video_status.task_id:
        task_result = TaskResult.objects.get(task_id=video_status.task_id)
        result = json.loads(task_result.result)  # Desserializando o JSON
        if task_result.status == 'SUCCESS':
            return render(request, 'video_analysis/results.html', {'emotion_counts': result})
        else:
            return JsonResponse({'status': task_result.status})
    else:
        return JsonResponse({'status': 'PENDING'})


def task_progress(request, task_id):
    task = AsyncResult(task_id)
    response_data = {
        'status': task.status,
    }
    if task.status == 'SUCCESS':
        video_status = VideoProcessingStatus.objects.get(task_id=task_id)
        response_data['video_id'] = video_status.id
    elif task.status == 'PROGRESS':
        response_data.update(task.info)
    return JsonResponse(response_data)
