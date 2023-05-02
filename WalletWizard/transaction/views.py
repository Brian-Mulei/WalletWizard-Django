from rest_framework import generics, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Transaction
from .serializers import TransactionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        """
        This view should return a list of all the transactions
        for the currently authenticated user.
        """
        user = self.request.user
        return Transaction.objects.filter(account__user=user)

    def perform_create(self, serializer):
        serializer.save(account__user=self.request.user)

    @action(detail=False, methods=['get'])
    def income(self, request):
        user = self.request.user
        transactions = Transaction.objects.filter(
            account__user=user,
            transaction_type='income'
        )
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def expense(self, request):
        user = self.request.user
        transactions = Transaction.objects.filter(
            account__user=user,
            transaction_type='expense'
        )
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)
