from rest_framework import serializers
from .models import UserTask

class TaskSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(source="user_id.username")
    class Meta:
        model = UserTask
        fields = ('user_id','task')