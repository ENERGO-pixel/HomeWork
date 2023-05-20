from decimal import Decimal
from datetime import timedelta
from datetime import date
from django.db import models

class Catagory(models.Model):
    name = models.CharField(null=False, max_length=100)
    def __str__(self):
        return self.name
class Products(models.Model):
    name = models.CharField(max_length=100, null=False)
    catagoryid=models.ForeignKey(Catagory,on_delete=models.CASCADE, null=True)
    price=models.DecimalField(decimal_places=2, max_digits=10, default=1)
    def __str__(self):
        return self.name
class Order(models.Model):
    date = models.DateTimeField()
    userid=models.PositiveBigIntegerField()
    productid=models.ForeignKey(Products,on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.productid
class Wallet(models.Model):
    userid = models.PositiveBigIntegerField(unique=True)
    balance=models.DecimalField(decimal_places=2, max_digits=100, default=0)
    def __str__(self):
        return (self.userid)
class categoryforwashing(models.Model):
    namecat = models.CharField(max_length=100, null=False)
    price = models.DecimalField(decimal_places=2, max_digits=100, default=0)
    def __str__(self):
        return (self.namecat)
class description(models.Model):
    nameid=models.ForeignKey(categoryforwashing,on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=2000, null=False)
class JustUser(models.Model):
    companyORuser = models.CharField(max_length=100, null=True)
    userid = models.PositiveBigIntegerField(unique=True)
class timewashing(models.Model):
    endtime = models.DateTimeField(auto_now=False, blank=True, null=True)
    userid=models.PositiveBigIntegerField()
class AutoRegister(models.Model):
    userid = models.PositiveBigIntegerField()
    login=models.CharField(max_length=100, null=False)
    password=models.CharField(max_length=100, null=False)
    authorized = models.BooleanField(default=False)




