from api.models import Transactions
from api.serializers import TransactionSerializers
from rest_framework import generics


class TransactionList(generics.ListCreateAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializers


class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializers