# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Chat, Message
from django.contrib.auth.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.chat_id = self.scope['url_route']['kwargs']['chat_id']
        self.chat_room = f'chat_{self.chat_id}'

        # Check if the user is part of the chat
        chat = Chat.objects.get(id=self.chat_id)
        if self.user in [chat.user1, chat.user2]:
            # Join the WebSocket group for this chat
            await self.channel_layer.group_add(self.chat_room, self.channel_name)
            await self.accept()

    async def disconnect(self, close_code):
        # Leave the WebSocket group for this chat
        await self.channel_layer.group_discard(self.chat_room, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_text = text_data_json['message']
        sender = self.user

        # Get the chat object
        chat = Chat.objects.get(id=self.chat_id)

        # Save the message to the database
        message = Message.objects.create(chat=chat, sender=sender, text=message_text)

        # Send the message to the WebSocket group
        await self.channel_layer.group_send(self.chat_room, {
            'type': 'chat_message',
            'message': message.text,
            'sender': sender.username,
        })

    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']

        # Send the message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
        }))
