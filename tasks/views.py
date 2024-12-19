from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Task
from .serializers import TaskSerializer
from users.models import TaskUser


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_all_tasks(request):
    print("USER IS:",request.user)
    tasks = Task.objects.filter(user=1) # Show only User tasks 
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@permission_classes([IsAdminUser])
def get_admin_tasks(request):
    print("USER IS:",request.user)
    tasks = Task.objects.all() # Show all tasks
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

# Register(Better to put this end point in User Template):
@api_view(['POST'])
def register(request):
   user = TaskUser.objects.create_user(
               username=request.data['username'],
               email=request.data['email'],
               password=request.data['password']
           )
   user.is_active = True
   #user.is_staff = True
   user.save()
   return Response("New user born")