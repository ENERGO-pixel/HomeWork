# Generated by Django 4.1.4 on 2022-12-08 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_remove_fruits_and_vegetables_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='fruits_and_vegetables',
            name='type',
            field=models.CharField(choices=[('Fr', 'Fruit'), ('Ve', 'Vegetable')], default='Fr', max_length=2),
        ),
    ]
