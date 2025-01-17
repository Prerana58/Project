# chat_project/asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path  # Import 'path'
from chat import consumers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_project.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Standard HTTP routing
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path('ws/chat/<int:chat_id>/', consumers.ChatConsumer.as_asgi()),  # WebSocket route
        ])
    ),
})
