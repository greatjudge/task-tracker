from rest_framework import serializers
from .models import Task, TaskSection, TaskStatus
from django.contrib.auth import get_user_model


User = get_user_model()


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'

    def validate(self, data):
        # print(data['section'].user, data['status'].user, data['user'].id)
        user = self.context['request'].user
        if data['section'].user.id != user.id:
            raise serializers.ValidationError('Cannot create task with section created by another user')
        if data['status'].user.id != user.id:
            raise serializers.ValidationError('Cannot create task with status created by another user')
        return data


class TaskSectionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = TaskSection
        fields = '__all__'


class TaskStatusSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = TaskStatus
        fields = '__all__'

