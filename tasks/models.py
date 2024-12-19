from django.conf import settings
from django.db import models
from users.models import TaskUser

class Task(models.Model):
    name = models.CharField(max_length=255)                   # Task name
    deadline = models.DateField()                             # Task deadline date
    done = models.BooleanField(default=False)                 # Done status (True/False)
    user = models.ForeignKey(TaskUser, on_delete=models.CASCADE)  # Link to the User model
    
    def __str__(self):
        return self.name