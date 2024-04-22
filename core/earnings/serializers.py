from rest_framework import serializers
from .models import Earnings


class EarningsSerializer(serializers.ModelSerializer):
    category_title = serializers.ReadOnlyField(source='category.title')

    class Meta:
        model = Earnings
        fields = ['category_title', 'amount', 'currency', 'comment']
