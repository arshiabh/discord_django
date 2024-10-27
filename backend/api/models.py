from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    

class Massage(models.Model):
    # user = User
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.body[0:50]
