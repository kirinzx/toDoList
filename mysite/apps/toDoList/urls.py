from django.urls import path
from . import views

urlpatterns = [
    path('', views.toDoList, name='home'),
    path('api/user/<int:pk>/task', views.TaskList.as_view()),
    path('api/user/task', views.TaskCreate.as_view()),
    path('api/user/task/<int:pk>', views.TaskDelete.as_view()),
]
