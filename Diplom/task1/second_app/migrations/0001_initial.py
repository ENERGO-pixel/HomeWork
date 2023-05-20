# Generated by Django 4.1.4 on 2022-12-12 07:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.PositiveIntegerField(validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(5)])),
                ('financing', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
