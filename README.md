# Lesson48_Login_Frontend

29.10.2024-01:58

## Commands schema on VScode:
pip install django-cors-headers
pip freeze > requirements.txt

In ChatGPT:
I will give you views.py and models.py in my backend django rest framework.
please add a simple html js screen that will show a task list. no login needed.
use bootstrap style and axios async await.
views.py:
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Task
from .serializers import TaskSerializer
from users.models import TaskUser


@api_view(['GET'])
@permission_classes([IsAuthenticated]) # Authentication for this end point(If logged in)
def get_all_tasks(request):
    print("logged in user is:",request.user) # request.user = logged in user
    tasks = Task.objects.filter(user=request.user) # Show only User tasks 
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

models.py:
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

## Virtual Environment
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
pip freeze > requirements.txt
deactivate

# Django
## Initialize application:
pip install django
django-admin startproject (Name of project)  .  (Don't forget space and dot at the end!!!)
py manage.py startapp (Name of folder)
py manage.py runserver

## Admin:
py manage.py runserver
py manage.py createsuperuser

## Migration to Database:
py manage.py makemigrations  
py manage.py migrate

## Shell,I-python commends:
pip install ipython
py manage.py shell

## Adding to Database:
from courts.models import Court
c = Court(number1)
c.save()

from members.models import Member
m = Member(firstname='Emil', lastname='Refsnes', phone='111111')
m.save()

court = Court.objects.first()
m = Member(firstname='Emil', lastname='Refsnes', phone='111111', court=court)
m.save()
court2 = Court.objects.get(id=2)
m = Member(firstname='Emil', lastname='Refsnes', phone='111111', court=court2)
m.save()

## Delete from Database:
x = Member.objects.all()[0]       [0] --Witch index to delete
x.firstname                       Check the name of the index to delete(Optional)
x.delete()

## Delete all:
Member.objects.all().delete()

## Change id:
x = Member.objects.all()[0]
x.id                         
x.id = 1 
x.save()

## Reset the Auto-increment Sequence of ID in DB:
Member.objects.all().delete()
from django.db import connection
with connection.cursor() as cursor:
    cursor.execute('DELETE FROM sqlite_sequence WHERE name="@@@@"')     (change: "@@@" to the table name in DB, Example:"members_member") 

## Work with Ipython Shell
1. In main project folder, in settings folder add the line: SHELL_PLUS ='ipython'
2. pip install ipython
3. python manage.py shell
4. exit()

## Uninstall all packages in a virtual environment
pip freeze > requirements.txt
pip freeze | xargs pip uninstall -y
deactivate
pip cache purge
DELETE VENV FILE!!!

## Remove last commit on GIT
git reset HEAD~1
git push -f origin main