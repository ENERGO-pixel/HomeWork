from django.db import models

# Create your models here.
class Fruits_and_Vegetables(models.Model):
    name = models.CharField(max_length=100)
    Fruit='Fr'
    Vegetable='Ve'
    type_CHOICES= [
        (Fruit,'Fruit'),
        (Vegetable,'Vegetable')
        ]
    color = models.CharField(max_length=100)
    type=models.CharField(
        max_length=2,
        choices=type_CHOICES,
        default=Fruit
    )
    calories = models.DecimalField(decimal_places=2, max_digits=10)
    about = models.TextField(max_length=1000)
    price = models.DecimalField(decimal_places=2, max_digits=10)