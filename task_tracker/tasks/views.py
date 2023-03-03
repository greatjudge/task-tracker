from .serializers import TaskSerializer, TaskStatusSerializer, TaskSectionSerializer
from .models import Task, TaskSection, TaskStatus
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class TasksList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskSectionList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSectionSerializer

    def get_queryset(self):
        return TaskSection.objects.filter(user=self.request.user)


class TaskSectionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSectionSerializer

    def get_queryset(self):
        return TaskSection.objects.filter(user=self.request.user)


class TaskStatusList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskStatusSerializer

    def get_queryset(self):
        return TaskStatus.objects.filter(user=self.request.user)


class TaskStatusDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskStatusSerializer

    def get_queryset(self):
        return TaskStatus.objects.filter(user=self.request.user)

