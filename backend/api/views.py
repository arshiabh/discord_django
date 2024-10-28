from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomCreation
from django.db.models import Q



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



def createRoom(request):
    if request.method == 'POST':
        form = RoomCreation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RoomCreation()
    return render(request, 'api/create_form.html', {'form':form})



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



def DeleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('index') 
    return render(request, 'api/delete.html', {"obj":room})