from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from earnings.serializers import EarningsSerializer

from earnings.models import Earnings


@api_view(['GET'])
def get_earnings(request):
    earnings = Earnings.objects.all()
    serializer = EarningsSerializer(earnings, many=True)
    return Response(serializer.data)
    # earn = Earnings.objects.all()
    # earn_data = []
    #
    # for e in earn:
    #     earn_data = {
    #         "category": e.category,
    #         "amount": e.amount,
    #         "currency": e.currency,
    #         "comment": e.comment,
    #     }
    #
    #
    # return Response(earn_data)
