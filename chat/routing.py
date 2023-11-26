from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    # Chat routing
    re_path(r'ws/socket-server/', consumers.ChatConsumer.as_asgi())
]