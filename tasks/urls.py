from django.contrib import admin
from django.urls import include, path
from tasks import views

urlpatterns = [
    path('', views.get_all_tasks, name="get_all_tasks"),
    path('admin_tasks/', views.get_admin_tasks, name="get_admin_tasks"),
    path('register/', views.register, name="register"),
]