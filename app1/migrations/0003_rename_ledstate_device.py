# Generated by Django 5.0.7 on 2025-02-27 05:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_ledstate_is_active'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LedState',
            new_name='Device',
        ),
    ]
