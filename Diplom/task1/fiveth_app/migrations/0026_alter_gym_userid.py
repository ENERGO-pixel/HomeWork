# Generated by Django 4.1.4 on 2023-01-19 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiveth_app', '0025_alter_gym_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gym',
            name='userid',
            field=models.PositiveBigIntegerField(verbose_name=1),
        ),
    ]
