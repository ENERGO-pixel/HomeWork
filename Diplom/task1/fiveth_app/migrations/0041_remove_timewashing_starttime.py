# Generated by Django 4.1.4 on 2023-04-18 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fiveth_app', '0040_alter_timewashing_endtime_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timewashing',
            name='starttime',
        ),
    ]
