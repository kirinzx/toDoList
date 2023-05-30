from django.urls import path
from . import views

urlpatterns = [
    path('',views.toDoList,name='home'),
    path('api/user/<int:user>/task',views.Task.as_view({'post':'create','get':'list'})),
    path('api/user/task',views.Task.as_view({'post':'create'})),
]