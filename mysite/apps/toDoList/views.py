from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from apps.authentication.models import User
from rest_framework.authtoken.models import Token
from .models import UserTask
from .serializers import TaskSerializer


@login_required
def toDoList(request):
    currentUser = request.user
    userTasks = UserTask.objects.filter(user_id=currentUser)
    return render(request, 'toDoList.html', context={"user_id": request.user.id, 'userTasks': userTasks})

class TaskCreate(generics.CreateAPIView):
    queryset = UserTask.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

class TaskList(generics.ListAPIView):
    queryset = UserTask.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

class TaskDelete(generics.DestroyAPIView):
    queryset = UserTask.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)