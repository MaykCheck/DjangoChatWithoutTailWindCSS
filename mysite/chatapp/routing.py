from django.urls import path
from chatapp import consumers

websocket_urlpatterns = [
    path('ws/<str:room_name>/',consumers.ChatConsumer.as_asgi()),
]