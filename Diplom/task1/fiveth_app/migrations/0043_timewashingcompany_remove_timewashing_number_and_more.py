# Generated by Django 4.1.4 on 2023-04-26 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiveth_app', '0042_timewashing_number_timewashing_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='timewashingcompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endtime', models.DateTimeField(blank=True, null=True)),
                ('userid', models.PositiveBigIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='timewashing',
            name='number',
        ),
        migrations.RemoveField(
            model_name='timewashing',
            name='status',
        ),
    ]
