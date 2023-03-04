from django.contrib import admin
from django.urls import path
from .views import (
    RegisterView, UserDetail,
    ChangePasswordView, UpdateProfileView
)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('<int:pk>/', UserDetail.as_view(), name='user_detail'),
    path('change_password/<int:pk>/',
         ChangePasswordView.as_view(),
         name='change_password'),
    path('update_profile/<int:pk>/',
         UpdateProfileView.as_view(),
         name='update_profile'),

]
