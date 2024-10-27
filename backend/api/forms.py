from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Room
from django import forms


class RoomCreation(ModelForm):
    
    class Meta:
        model = Room
        fields = '__all__' 