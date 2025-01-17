# chat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_home, name='chat_home'),
    path('signup/', views.sign_up, name='sign_up'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.log_out, name='logout'),  
    path('chat/<int:user_id>/', views.chat_with_user, name='chat_with_user'),
]
