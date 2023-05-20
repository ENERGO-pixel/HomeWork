# Generated by Django 4.1.4 on 2023-04-26 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fiveth_app', '0043_timewashingcompany_remove_timewashing_number_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='timewashingcompany',
        ),
        migrations.AddField(
            model_name='timewashing',
            name='company_or_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='timewashings', to='fiveth_app.justuser'),
        ),
    ]
