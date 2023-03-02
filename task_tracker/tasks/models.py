from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

TASK_SECTION = [('personal', 'Personal'),
                ('work', 'Work'),
                ('study', 'Study')
               ]

TASK_STATUS = [('todo', 'To Do'),
               ('in_progress', 'In Progress'),
                ('done', 'Done')
              ]

class TaskSection(models.Model):
    title = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default="#ffffff")
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class TaskStatus(models.Model):
    title = models.CharField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    section = models.ForeignKey(TaskSection, null=True, on_delete=models.SET_NULL)  # FIX ?
    # status = models.ForeignKey(TaskStatus, null=True, on_delete=models.SET_NULL)  # FIX
    status = models.CharField(choices=TASK_STATUS, blank=True)  # FIX
    priority = models.IntegerChoices('Priority', 'ONE TWO THREE FOUR FIVE')
    linked_tasks = models.ManyToManyField('self', blank=True,
                                          symmetrical=False,
                                          related_name='required_by')
    start_datetime = models.DateTimeField()
    due_datetime = models.DateTimeField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
