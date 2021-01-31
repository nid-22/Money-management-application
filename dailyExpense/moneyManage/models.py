from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class userRegister(User):
    age = models.IntegerField()
    contact = models.IntegerField()

class Income(models.Model):
    income = models.IntegerField()
    #income_date = models.DateField( default=date.today)
    income_date = models.DateField( auto_now=True)
    income_type = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    user = models.ForeignKey(userRegister, on_delete=models.CASCADE)

    class Meta:
        db_table = 'income'

class Expense(models.Model):
    expense = models.IntegerField()
    #expense_date = models.DateField( default=date.today)
    expense_date = models.DateField(auto_now=True)
    expense_type = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    user = models.ForeignKey(userRegister, on_delete = models.CASCADE)

    class Meta:
        db_table = 'expense'
        