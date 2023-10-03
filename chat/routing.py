from django.urls import re_path
from .consumers import ChatConsumer

websocket_urlpatterns_=[
     re_path(r'ws/chaa/(?P<nome_sala>/W+)/$', ChatConsumer),
]