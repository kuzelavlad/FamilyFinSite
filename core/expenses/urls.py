from django.urls import path
from expenses.views import get_expenses

urlpatterns = [

    path('api/expenses/', get_expenses, name='get_expenses'),
]
