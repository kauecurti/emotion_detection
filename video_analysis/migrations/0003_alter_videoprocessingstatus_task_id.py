# Generated by Django 5.0.6 on 2024-05-17 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_analysis', '0002_remove_videoprocessingstatus_completed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoprocessingstatus',
            name='task_id',
            field=models.CharField(max_length=255),
        ),
    ]
