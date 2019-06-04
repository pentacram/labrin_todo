from django.db import models
from django.contrib.auth.models import User



class Todo(models.Model):
    users = models.ManyToManyField(User)
    task = models.TextField(null=True, blank=True)
    starttime = models.DateField(null=True, blank=True)
    deaddate = models.DateField(null=True, blank=True)
    deadtime = models.TimeField(null=True, blank=True)
    status = models.BooleanField()

    def __str__(self):
        return f"{self.task} {self.starttime} {self.deaddate} {self.deadtime} {self.status}"



