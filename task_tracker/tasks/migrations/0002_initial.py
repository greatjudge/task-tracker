# Generated by Django 4.1.7 on 2023-03-02 22:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="taskstatus",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="task_statuses",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="tasksection",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="task_sections",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="linked_tasks",
            field=models.ManyToManyField(
                blank=True, related_name="required_by", to="tasks.task"
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="section",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="tasks.tasksection"
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="status",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="tasks.taskstatus"
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]