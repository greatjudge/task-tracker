from rest_framework import serializers
from .models import Task, TaskSection, TaskStatus
from django.contrib.auth import get_user_model


User = get_user_model()


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'

    def validate_linked_tasks(self, attrs):
        linked_task_userids = set([task.user.id for task in attrs])  # does it effective getting from db?
        if (len(linked_task_userids) != 1
                or linked_task_userids.pop() != self.context['request'].user.id):
            raise serializers.ValidationError('Related tasks must belong to the user')
        return attrs

    def validate(self, data):
        user = self.context['request'].user
        if data['section'].user.id != user.id:
            raise serializers.ValidationError('Cannot create task with section created by another user')
        if data['status'].user.id != user.id:
            raise serializers.ValidationError('Cannot create task with status created by another user')

        start_datetime = data['start_datetime'] if 'start_datetime' in data \
            else self.instance.start_datetime
        due_datetime = data.get('due_datetime')
        if due_datetime is None:
            if self.instance is not None and hasattr(self.instance, 'due_datetime'):
                due_datetime = self.instance.due_datetime
        if due_datetime is not None and start_datetime > due_datetime:
            raise serializers.ValidationError("start_datetime could not be greater than due_datetime")
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

