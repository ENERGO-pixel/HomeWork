# Generated by Django 4.1.4 on 2023-01-11 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiveth_app', '0006_wallet_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='wallet',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=100),
        ),
    ]