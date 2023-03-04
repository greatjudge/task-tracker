from django.contrib import admin
from .models import Task, TaskSection, TaskStatus

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'status', 'section')


@admin.register(TaskSection)
class TaskSectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user')


@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user')
