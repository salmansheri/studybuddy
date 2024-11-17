from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout


def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        try:
            user=User.objects.get(username=username)
            print(user)

        except:
            messages.error(request, "user doesnt exist")

        user = authenticate(request, username=username, password=password)
        if user is not None: 
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Username or password does'nt exist")
    context={}
    return render(request, "app/auth.html",context)

def home(request):
    query= request.GET.get('q') if request.GET.get('q') != None else ""
    rooms=Room.objects.filter(
        Q(topic__name__icontains=query) |
        Q(name__icontains=query) |
        Q(description__icontains=query)

    )
    room_count = rooms.count()
    topics = Topic.objects.all()
    context={"rooms": rooms, "topics": topics, "room_count": room_count}
    return render(request, "app/home.html", context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {"room": room.name}
    return render(request, "app/room.html", context) 

def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form=RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, 'components/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context= {"form": form}
    return render(request, 'components/room_form.html', context)

def deleteroom(request, pk):
    room=Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'app/delete.html', {'obj': room})


