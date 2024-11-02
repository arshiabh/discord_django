from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Room
from django import forms

class RoomCreation(ModelForm):
    
    class Meta:
        model = Room
        fields = '__all__'
        #exclude mikonim chon to form nayad host yeki dg entkhb konim
        #view handelesh karidim ke host = user gozashtim
        exclude = ['host','participants'] 


class UserForm(ModelForm):

    class Meta:
        model = User

        fields = ['username','email']