from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomCreation
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate, logout 
from django.contrib.auth.decorators import login_required



def LoginPage(request):

    #if already is , redirect it 
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'user does not exits!')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'username or password does not exist!')

    context = {}
    return render(request, 'api/login_register.html', context)



def LogoutPage(request):
    logout(request)
    return redirect('index')




def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q)
                                )
    room_count = rooms.count()
    topics = Topic.objects.all()
    return render(request, 'api/home.html',{"rooms":rooms,'topics':topics,'room_count':room_count})



def room(request,pk):
    room = Room.objects.get(id=pk)            
    context = {
        'room':room
    }
    return render(request, 'api/room.html', context)



@login_required(login_url='login')
def createRoom(request):
    if request.method == 'POST':
        form = RoomCreation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RoomCreation()
    return render(request, 'api/create_form.html', {'form':form})



@login_required(login_url='login')
def UpdateRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        form = RoomCreation(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RoomCreation(instance=room)

    context = {
        'form': form
    }
    return render(request, 'api/create_form.html', context)



@login_required(login_url='login')
def DeleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('index') 
    return render(request, 'api/delete.html', {"obj":room})