from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import TaskUser

admin.site.register(TaskUser, UserAdmin)