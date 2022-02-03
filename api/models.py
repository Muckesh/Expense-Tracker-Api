from hashlib import blake2s
from django.db import models

# Create your models here.

class Transactions(models.Model):
    transaction = models.CharField(max_length=500,null=True,blank=True)
    amount = models.IntegerField(null=True,blank=True)
    isIncome=models.BooleanField(default=False)

    def __str__(self):
        return self.transaction