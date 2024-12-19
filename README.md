# Lesson48_Login_Frontend

29.10.2024-00:51

## Commands schema on VScode:
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
python.exe -m pip install --upgrade pip
python manage.py makemigrations tasks
py manage.py migrate
py manage.py createsuperuser

ChatGPT:
1. THIS IS THE VIEWS.PY PLEASE MAKE A FRONT END THAT WILL SHOW THE TASKS
2. ADD A LOGIN FORM + CALL TO LOGIN ENDPOINT USING AXIOS ASYNC
3. SAVE TOKEN RECEIVED TN LOCALSTORAGE
4. CALL GET TASKS USING TOKEN AND AXIOS ASYNC

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