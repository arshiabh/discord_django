from django.shortcuts import render
from .models import Room


# rooms = [
#     {'id':1, "name":"frontend"},
#     {'id':2, "name":"learn back"},
#     {'id':3, "name":"learn angular"}
# ]

def home(request):
    rooms = Room.objects.all()
    return render(request, 'api/home.html',{"rooms":rooms})


def room(request,pk):
    room = Room.objects.get(id=pk)            
    context = {
        'room':room
    }
    return render(request, 'api/room.html', context)