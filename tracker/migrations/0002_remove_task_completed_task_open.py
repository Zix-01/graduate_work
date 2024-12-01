# Generated by Django 5.1.3 on 2024-12-01 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tracker", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="task",
            name="completed",
        ),
        migrations.AddField(
            model_name="task",
            name="open",
            field=models.BooleanField(default=True),
        ),
    ]
