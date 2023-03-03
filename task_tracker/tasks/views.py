from .serializers import TaskSerializer, TaskStatusSerializer, TaskSectionSerializer
from .models import Task, TaskSection, TaskStatus
from rest_framework import generics


class TasksList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskSectionList(generics.ListAPIView):
    serializer_class = TaskSectionSerializer

    def get_queryset(self):
        return TaskSection.objects.filter(user=self.request.user)


class TaskSectionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSectionSerializer

    def get_queryset(self):
        return TaskSection.objects.filter(user=self.request.user)


class TaskStatusList(generics.ListAPIView):
    serializer_class = TaskStatusSerializer

    def get_queryset(self):
        return TaskStatus.objects.filter(user=self.request.user)


class TaskStatusDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskStatusSerializer

    def get_queryset(self):
        return TaskStatus.objects.filter(user=self.request.user)

