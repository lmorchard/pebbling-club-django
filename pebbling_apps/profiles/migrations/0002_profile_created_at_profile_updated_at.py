# Generated by Django 5.1.6 on 2025-02-08 00:05

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="created_at",
            field=models.DateTimeField(
                default=django.utils.timezone.now, editable=False
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
