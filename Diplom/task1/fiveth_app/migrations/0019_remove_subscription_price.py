# Generated by Django 4.1.4 on 2023-01-18 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fiveth_app', '0018_delete_testtime_remove_subscription_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='price',
        ),
    ]