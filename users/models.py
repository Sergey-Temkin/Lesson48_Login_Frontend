from django.contrib.auth.models import AbstractUser
from django.db import models

class TaskUser(AbstractUser):
    favorite_color = models.CharField(max_length=30,null=True)  
