import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class VideoConsumer(WebsocketConsumer):
    def connect(self):
        self.video_id = self.scope['url_route']['kwargs']['video_id']
        self.room_group_name = f'video_{self.video_id}'

        
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        progress = text_data_json['progress']

      
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'video_progress',
                'progress': progress
            }
        )

    def video_progress(self, event):
        progress = event['progress']

       
        self.send(text_data=json.dumps({
            'progress': progress
        }))
