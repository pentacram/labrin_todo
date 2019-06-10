from django.db import models
from django.contrib.auth.models import User



class Todo(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.TextField(null=True, blank=True)
    starttime = models.DateField(null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField()

    def __str__(self):
        return f"{self.task} {self.starttime} {self.deadline} {self.status} {self.users}"



