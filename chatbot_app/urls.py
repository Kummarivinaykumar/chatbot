# chatbot_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('api/chatbot/', views.chatbot_api, name='chatbot_api'),
]

# chatbot_app/urls.py

urlpatterns = [
    path('api/chatbot/', views.chatbot_api, name='chatbot_api'),
    path('chat/', views.chat_view, name='chat_view'),
]
