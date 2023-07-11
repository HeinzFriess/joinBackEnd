import datetime
from django.conf import settings
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=300)
    def __str__(self):
        return f'{self.id} {self.name}'

class Priority(models.Model):
    name = models.CharField(max_length=300)
    def __str__(self):
        return f'{self.id} {self.name}'

class State(models.Model):
    name = models.CharField(max_length=300)
    def __str__(self):
        return f'{self.id} {self.name}'
class Ticket(models.Model):
    title = models.CharField(max_length=300)
    category =  models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.TextField(blank= True)
    priority = models.ForeignKey(Priority,on_delete=models.CASCADE)
    status = models.ForeignKey(State,on_delete=models.CASCADE)
    maintask = models.BooleanField(default=False)
    assigned = models.CharField(max_length=100)
    date = models.DateField(default=datetime.date.today)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateField(default=datetime.date.today)
    def __str__(self):
        return f'{self.id} {self.title}'
