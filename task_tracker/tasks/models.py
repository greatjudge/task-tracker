from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

TASK_SECTION = [
    ('personal', 'Personal'),
    ('work', 'Work'),
    ('study', 'Study')
]

TASK_STATUS = [
    ('todo', 'To Do'),
    ('in_progress', 'In Progress'),
    ('done', 'Done')
]

DEFAULT_SECTION = {'title': 'Личное',
                   'color': '#ffffff'}
DEFAULT_STATUS = {'title': 'Сделать'}



class TaskSection(models.Model):
    title = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default="#ffffff")
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
    # status = models.CharField(choices=TASK_STATUS, blank=True)  # FIX
    priority = models.IntegerChoices('Priority', 'ONE TWO THREE FOUR FIVE')
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
