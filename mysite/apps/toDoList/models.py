from django.db import models
from apps.authentication.models import User
class UserTask(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    task = models.TextField()
    def __str__(self):
        return self.task
