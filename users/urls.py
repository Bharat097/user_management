from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_users, name='list_users'),
    path('register/', views.register, name='register'),
    path('login/', views.log_in_user, name='login'),
    path('logout/', views.log_out_user, name='logout'),
    path('edit_user/<str:user_id>', views.edit_user, name='edit_user'),
]
