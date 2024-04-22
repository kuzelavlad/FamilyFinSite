from rest_framework.decorators import api_view
from rest_framework.response import Response
from expenses.serializers import ExpensesSerializer
from expenses.models import Expenses


@api_view(['GET'])
def get_expenses(request):
    earnings = Expenses.objects.all()
    serializer = ExpensesSerializer(earnings, many=True)
    return Response(serializer.data)
