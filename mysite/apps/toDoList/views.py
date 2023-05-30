from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from apps.authentication.models import User
from rest_framework.authtoken.models import Token
from .models import UserTask
from .serializers import TaskSerializer


@login_required
def toDoList(request):
    currentUser = request.user
    userTasks = UserTask.objects.filter(user_id=currentUser)
    return render(request, 'toDoList.html', context={"user_id": request.user.id, 'userTasks': userTasks})


def checkIfUserExists(user_id):
    if not User.objects.filter(id=user_id).exists():
        return False
    return True

def checkAuth(key, user_id):
    if Token.objects.filter(key=key).exists():
        token = Token.objects.get(key=key)
        if token.user != User.objects.get(id=user_id):
            return False
        return True
    return False

class Task(viewsets.ViewSet):
    def create(self, request):
        user_id = request.data.get("user")
        task = request.data.get("task")
        if not checkIfUserExists(user_id):
            return Response(data={"detail: user doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
        createdTask = UserTask.objects.create(
            user_id=User.objects.get(id=user_id), task=task)
        serializer = TaskSerializer(createdTask)
        return Response(data=serializer.data)

    def list(self, request, user=None):
        if not checkIfUserExists(user):
            return Response(data={"detail: user doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
        tasks = UserTask.objects.filter(user_id=User.objects.get(id=user))
        serializer = TaskSerializer(tasks, many=True)
        return Response(data=serializer.data)
