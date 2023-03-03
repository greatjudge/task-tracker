from django.contrib import admin
from django.urls import path
from .views import RegisterView, UsersList, UserDetail

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('/', UsersList.as_view(), name='users_list'),
    path('/<int:pk>', UserDetail.as_view(), name='user_detail')
]
