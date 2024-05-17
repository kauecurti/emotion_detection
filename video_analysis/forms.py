from django import forms
from .models import VideoProcessingStatus

class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = VideoProcessingStatus
        fields = ['video']
