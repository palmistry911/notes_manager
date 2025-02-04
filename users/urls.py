from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>/', views.UserItem.as_view(), name='user_item'),
]