from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('tasks/', TasksList.as_view()),
    path('tasks/<int:pk>/', TaskDetail.as_view()),

    path('statuses/', TaskStatusList.as_view()),
    path('sections/', TaskSectionList.as_view()),
]