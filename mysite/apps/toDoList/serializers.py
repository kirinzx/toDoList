from rest_framework import serializers
from .models import UserTask


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTask
        fields = "__all__"
