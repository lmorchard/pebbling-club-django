# Generated by Django 5.1.6 on 2025-02-22 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("feeds", "0002_alter_feed_created_at_alter_feed_updated_at_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="feeditem",
            name="json",
            field=models.JSONField(blank=True, null=True),
        ),
    ]
