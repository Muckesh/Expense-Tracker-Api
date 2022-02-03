from decimal import Clamped
import imp
from pyexpat import model
from django.forms import fields
from rest_framework import serializers
from api import models

class TransactionSerializers(serializers.ModelSerializer):
    class Meta:
        fields=(
            'id',
            'transaction',
            'amount',
            'isIncome'
        )
        model = models.Transactions
        fields='__all__'