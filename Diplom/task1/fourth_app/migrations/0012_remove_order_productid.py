# Generated by Django 4.1.4 on 2023-01-17 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fourth_app', '0011_order_subid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='productid',
        ),
    ]