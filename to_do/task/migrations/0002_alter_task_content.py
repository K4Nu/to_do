# Generated by Django 4.2.11 on 2024-04-29 14:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="content",
            field=models.CharField(max_length=1500),
        ),
    ]