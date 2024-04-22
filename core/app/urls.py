from django.urls import path
from app.views import get_users, user_login, register

urlpatterns = [

    path('api/users/', get_users, name='get_users'),
    path('registration',register, name='register'),
    path('login/', user_login, name='user_login'),
]
