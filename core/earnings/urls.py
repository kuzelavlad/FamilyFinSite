from django.urls import path
from earnings.views import get_earnings

urlpatterns = [

    path('api/earnings/', get_earnings, name='get_earnings'),
]
