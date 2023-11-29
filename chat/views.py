import time
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rentapp.forms import MensajeForm

from rentapp.models import Amistad, Mensaje

def index(request):
    return render(request, "chat/index.html")

def room(request, room_name):
    # existe_amistad = Amistad.objects.filter()
    datos_amistad = list(Amistad.objects.values().order_by("-id"))
    datos = list(Mensaje.objects.values().filter(amistad_id = room_name).order_by("id"))


    resultado_amistad_rendador_renta = Amistad.objects.filter(id=room_name).values()

    form = MensajeForm()
    #return render(request, 'rentapp/insertar_mensaje.html', {'form': form, 'datos': datos, 'datos_amistad': datos_amistad })
    return render (request, "chat/room.html", {'resultado_amistad_rendador_renta':resultado_amistad_rendador_renta,'room_name': room_name, 'form': form, 'datos': datos, 'datos_amistad': datos_amistad })

    # if this is a POST request we need to process the form data
    # if request.method == 'POST':
    #     # create a form instance and populate it with data from the request:
    #     form = MensajeForm(request.POST)
    #     # check whether it's valid:
    #     if form.is_valid():
    #         # process the data in form.cleaned_data as required
    #         new_mensaje = Mensaje(
    #             amistad = form.cleaned_data['amistad'], 
    #             texto = form.cleaned_data['texto'],
    #             tipo = 'rendador',
    #             pub_date = time.strftime('%Y-%m-%d %I:%M')
    #              )
    #         new_mensaje.save()
    #         # redirect to a new URL:
    #         return HttpResponseRedirect(f'/chat/{room_name}')
    # # if a GET (or any other method) we'll create a blank form
    # else:


