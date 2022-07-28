from pickle import TRUE
from django.db import models

class Transaction(models.Model):
    drop_off = models.DateTimeField(blank=True)
    

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_num = models.IntegerField()
    last_four = models.IntegerField()
    email = models.CharField(max_length=200, blank=True)
    admin = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    transactions = models.ForeignKey(Transaction, on_delete=models.SET_NULL, null=TRUE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
