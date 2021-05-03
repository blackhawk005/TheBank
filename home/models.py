from django.db import models

# Create your models here.

class Customers(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    dob = models.DateField()
    contact_no = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    current_balance = models.IntegerField()

class Transactions(models.Model):
    sender = models.CharField(max_length=200)
    reciever = models.CharField(max_length=200)
    amount = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
