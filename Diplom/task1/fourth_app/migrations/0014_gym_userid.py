# Generated by Django 4.1.4 on 2023-01-19 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fourth_app', '0013_remove_order_subid_order_productid'),
    ]

    operations = [
        migrations.AddField(
            model_name='gym',
            name='userid',
            field=models.PositiveBigIntegerField(default=1),
        ),
    ]