from rest_framework import serializers
from .models import Expenses


class ExpensesSerializer(serializers.ModelSerializer):
    category_title = serializers.ReadOnlyField(source='category.title')

    class Meta:
        model = Expenses
        fields = ['category_title', 'amount', 'currency', 'comment']
