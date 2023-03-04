from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
    RegexValidator
)


User = get_user_model()


DEFAULT_SECTION = {'title': 'Личное',
                   'color': '#ffffff'}
DEFAULT_STATUS = {'title': 'Сделать'}


class TaskSection(models.Model):
    title = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default="#ffffff", validators=[
        RegexValidator(regex=r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$")
    ])
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='task_sections')

    def __str__(self):
        return self.title


class TaskStatus(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='task_statuses')

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    section = models.ForeignKey(TaskSection,
                                on_delete=models.CASCADE,
                                limit_choices_to={'user': models.F('user')})
    status = models.ForeignKey(TaskStatus,
                               on_delete=models.CASCADE,
                               limit_choices_to={'user': models.F('user')})
    priority = models.SmallIntegerField(validators=[MinValueValidator(1),
                                                    MaxValueValidator(5)],
                                        blank=True, null=True)
    linked_tasks = models.ManyToManyField('self', blank=True,
                                          symmetrical=False,
                                          related_name='required_by')
    start_datetime = models.DateTimeField()
    due_datetime = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
