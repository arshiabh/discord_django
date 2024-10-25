from django.shortcuts import render

rooms = [
    {'id':1, "name":"frontend"},
    {'id':2, "name":"learn back"},
    {'id':3, "name":"learn angular"}
]

def home(request):
    return render(request, 'api/home.html',{"rooms":rooms})


def room(request,pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
            
    context = {
        'room':room
    }
    return render(request, 'api/room.html', context)