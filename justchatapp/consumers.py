import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Room, PublicMessage
from django.contrib.auth.models import User


class ChatConsumer(WebsocketConsumer):

    def load_messages(self):
        messages = PublicMessage.objects.filter(room=self.room).order_by('timestamp')

        for message in messages:
            self.send(text_data=json.dumps({
                'type': 'chat_message',
                'message': message.content,
                'author': message.author,
            }))

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.room = Room.objects.filter(name=self.room_name)[0]

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
        self.load_messages()

    def disconnect(self, close_code):
        # send (nickname left the chat)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_disconnect',
                'nick': 'asjfbashj',
            }
        )  

        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # receive message from user
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        type = text_data_json['type']

        if type == 'chat_message':
            message = text_data_json['message']
            author = text_data_json['author']
            public_message = PublicMessage.objects.create(author=author, content=message, room=self.room)
            mess_id = public_message.id
            public_message.save()

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'author': author,
                }
            )

        if type == 'chat_join':
            nick = text_data_json['nick']
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat_join',
                    'nick': nick,
                }
            )           

    # send message to textarea in template
    def chat_message(self, event):
        message = event['message']
        author = event['author']

        self.send(text_data=json.dumps({
            'type': 'chat_message',
            'message': message,
            'author': author,
        }))

    def chat_join(self, event):
        nick = event['nick']
        self.send(text_data=json.dumps({
            'type': 'chat_join',
            'nick': nick
        }))    

    def chat_disconnect(self, event):
        nick = event['nick']
        self.send(text_data=json.dumps({
            'type': 'chat_disconnect',
            'nick': nick
        }))               


