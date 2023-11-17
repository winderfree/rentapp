import time
from django.http import HttpResponseRedirect
from django.shortcuts import render

from rentapp.forms import MensajeForm
from rentapp.models import Amistad, Mensaje

def index(request):
    return render(request, "chat/index.html")

def room(request, room_name):
    return render (request, "chat/room.html", {"room_name": room_name})
