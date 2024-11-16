from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm


# rooms = [
#         {"id": 1, "name": "lets learn python!"}, 
#         {"id": 2, "name": "Design with me"}, 
#         {"id": 3, "name": "Frontend Developers"}, 
#         ]
# Create your views here.
def home(request):
    rooms=Room.objects.all()
    return render(request, "app/home.html", {"rooms": rooms}) 

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
    context= {"form": form}
    return render(request, 'components/room_form.html', context)



