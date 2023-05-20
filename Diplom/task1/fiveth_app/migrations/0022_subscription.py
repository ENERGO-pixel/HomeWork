# Generated by Django 4.1.4 on 2023-01-18 09:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiveth_app', '0021_delete_subscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.PositiveBigIntegerField(unique=True)),
                ('geeks_field', models.DateField(default=datetime.date(2023, 1, 18))),
                ('end_time', models.DateField(default=datetime.date(2023, 1, 18))),
            ],
        ),
    ]
