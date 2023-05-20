# Generated by Django 4.1.4 on 2023-01-16 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fourth_app', '0006_wallet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('userid', models.PositiveBigIntegerField()),
                ('productid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fourth_app.products')),
            ],
        ),
    ]