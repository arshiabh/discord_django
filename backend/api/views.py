from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomCreation


def home(request):
    rooms = Room.objects.all().order_by('-updated')
    return render(request, 'api/home.html',{"rooms":rooms})


def room(request,pk):
    room = Room.objects.get(id=pk)            
    context = {
        'room':room
    }
    return render(request, 'api/room.html', context)


def createRoom(request):
    if request.method == 'POST':
        form = RoomCreation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RoomCreation()
    return render(request, 'api/create_form.html', {'form':form})