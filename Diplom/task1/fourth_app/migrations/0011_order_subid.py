# Generated by Django 4.1.4 on 2023-01-17 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fourth_app', '0010_subscription_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='subid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fourth_app.subscription'),
        ),
    ]
