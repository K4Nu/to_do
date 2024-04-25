from django.db import models
import datetime
from django.contrib.auth.models import User
import datetime

class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=1500)
    date_start=models.DateField(default=datetime.date.today)
    date_end=models.DateField(default=datetime.date.today)
    color=models.CharField(max_length=7)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title