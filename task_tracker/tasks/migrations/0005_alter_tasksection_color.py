# Generated by Django 4.1.7 on 2023-03-04 19:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0004_task_priority"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tasksection",
            name="color",
            field=models.CharField(
                default="#ffffff",
                max_length=7,
                validators=[
                    django.core.validators.RegexValidator(
                        regex="^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"
                    )
                ],
            ),
        ),
    ]
