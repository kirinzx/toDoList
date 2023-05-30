from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def toDoList(request):
    current_user = request.user
    username = current_user.username
    return render(request, 'toDoList.html', {'username': username})