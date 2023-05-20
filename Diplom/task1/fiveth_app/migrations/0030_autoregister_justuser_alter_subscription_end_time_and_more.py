# Generated by Django 4.1.4 on 2023-01-26 14:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiveth_app', '0029_remove_trainwithtrainer_nameid_trainwithtrainer_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.PositiveBigIntegerField(unique=True)),
                ('login', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='JustUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.PositiveBigIntegerField(unique=True)),
                ('companyORuser', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='subscription',
            name='end_time',
            field=models.DateField(default=datetime.date(2023, 1, 26)),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='geeks_field',
            field=models.DateField(blank=True, null=True),
        ),
    ]
