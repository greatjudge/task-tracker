from rest_framework import serializers
from .models import Task, TaskSection, TaskStatus


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskSection
        fields = '__all__'


class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = '__all__'

