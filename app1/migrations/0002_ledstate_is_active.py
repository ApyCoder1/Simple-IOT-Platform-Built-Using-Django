# Generated by Django 5.0.7 on 2025-02-27 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ledstate',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
