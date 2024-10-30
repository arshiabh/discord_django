from django.shortcuts import render, redirect
from .models import Room, Topic, Massage
from .forms import RoomCreation
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate, logout 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm 




def LoginPage(request):
    page = 'login'
    #if already is , redirect it 
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
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

    context = {'page':page}
    return render(request, 'api/login_register.html', context)



def registerPage(request):
    page = 'register'
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #commit mibandim ye user misazim az rosh ke usernamesh lower konim
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'an error occured during register')
    else:
        form = UserCreationForm()
    context = {'page':page,'form':form}
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
    messages = room.massage_set.all().order_by('-created')
    participants = room.participants.all()

    if request.method == 'POST':
        newm = Massage.objects.create(
            user = request.user,
            room = room,
            #get toe templates ke hast sakhtim
            body = request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', pk=room.id)


    context = {
        'room':room,
        "messagess":messages,
        'participants':participants
    }
    return render(request, 'api/room.html', context)



@login_required(login_url='login')
def DeleteMessege(request, pk):
    messege = Massage.objects.get(id=pk)
    if request.method == 'POST':
        messege.delete()
        return redirect('index') 
    return render(request, 'api/delete.html', {"obj":messege})




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