import time
# from asgiref.sync import sync_to_async
# import asyncio
from django.core.paginator import Paginator
# from geopy.geocoders import Nominatim
# from django.shortcuts import redirect, render
from django.shortcuts import  render
# from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.http import  HttpResponse, HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import logout

# filepath: /c:/Users/WinFree/Desktop/repo/rentapp/rentapp/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Renta
from .forms import RentaForm

# def editar_renta(request, renta_id):
#     renta = get_object_or_404(Renta, id=renta_id)
#     if request.method == 'POST':
#         form = RentaForm(request.POST, instance=renta)
#         if form.is_valid():
#             form.save()
#             return redirect('rentapp:detail', renta_id=renta.id)
#     else:
#         form = RentaForm(instance=renta)
#     return render(request, 'rentapp/editar_renta.html', {'form': form})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

# def insertar_mensaje(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = MensajeForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             new_mensaje = Mensaje(
#                 amistad = form.cleaned_data['amistad'],
#                 texto = form.cleaned_data['texto'],
#                 tipo = 'rendador',
#                 pub_date = time.strftime('%Y-%m-%d %I:%M')
#                  )
#             new_mensaje.save()
#             # redirect to a new URL:
#             return HttpResponseRedirect('/rentapp/insertar_mensaje/')
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         # print (datos)
#         form = MensajeForm()
#     return render(request, 'rentapp/insertar_mensaje.html', {'form': form, })

# def insertar_mensaje_rendatario(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = MensajeForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             new_mensaje = Mensaje(
#                 amistad = form.cleaned_data['amistad'],
#                 texto = form.cleaned_data['texto'],
#                 tipo = 'rendatario',
#                 pub_date = time.strftime('%Y-%m-%d %I:%M')
#                  )
#             new_mensaje.save()
#             # redirect to a new URL:
#             return HttpResponseRedirect('/rentapp/insertar_mensaje_rendatario/')
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         datos_amistad = list(Amistad.objects.values().order_by("-id"))
#         datos = list(Mensaje.objects.values().order_by("-id"))
#         # print (datos)
#         form = MensajeForm()
#     return render(request, 'rentapp/insertar_mensaje_rendatario.html', {'form': form, 'datos': datos, 'datos_amistad': datos_amistad })

# def insertar_amistad(request, usertario_id, userdador_id, renta_id):
#     existe_amistad = Amistad.objects.filter(usertario=usertario_id,userdador=userdador_id, renta=renta_id).values_list()
#     # if(existe_amistad):
#     #     return HttpResponse("Si existe")
#     # else:
#     #     return HttpResponse("No existe")
#     # return HttpResponse(existe_amistad[0][0])
#     if existe_amistad:
#           return HttpResponseRedirect(f"/chat/{existe_amistad[0][0]}")
#     else:
#           renta = Renta.objects.get(id=renta_id)
#           usertario = Usertario.objects.get(id=usertario_id)
#           userdador = Userdador.objects.get(id=userdador_id)

#           f = AmistadForm()
#           new_amistad = f.save(commit=False)
#           new_amistad.renta = renta
#           new_amistad.usertario = usertario #12
#           new_amistad.userdador = userdador #12,
#           new_amistad.relacion = f'{usertario}:{ renta}'
#           new_amistad.pub_date = time.strftime('%Y-%m-%d %I:%M')
#           new_amistad.save()
#           # get the last 'id'
#           obj = Amistad.objects.latest('id')
#           # redirect to a new URL:
#           return HttpResponseRedirect(f"/chat/{obj}")
   
def insertar_user(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            user = User(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
                email = form.cleaned_data['email'],
                tipo = form.cleaned_data['phone_number'], )
            user.set_password(form.cleaned_data['password'])
            user.save()

            return HttpResponseRedirect(f'/dashboard/{user.id}')
    # if a GET (or any other method) we'll create a blank form
    else:

        #datos = list(Usertario.objects.values().order_by("-id"))
        form = UserForm()
    mensajes = messages.success(request, "Por favor inicie session o cuenta nueva")

    return render(request, 'rentapp/insertar_user.html', {'mensajes':mensajes,'form': form})


def insertar_foto(request, renta_id):
    datos_fotos = list(Foto.objects.filter(renta=renta_id).order_by("-id"))
    renta_title = list(Renta.objects.filter(id=renta_id))
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FotoForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            new_foto = Foto(
                renta = form.cleaned_data['renta'],
                image_renta = form.cleaned_data['image_renta'],
                name_foto_renta = form.cleaned_data['name_foto_renta'])
            new_foto.save()
            # obj = Foto.objects.latest('renta')
            # renta_id = obj
            # redirect to a new URL:
            return HttpResponseRedirect(f'/insertar_foto/{renta_id}')
    # if a GET (or any other method) we'll create a blank form
    else:
        # obj = Foto.objects.latest('renta')
        form = FotoForm()
        # datos_fotos = list(Foto.objects.all().order_by("-id"))
    return render(request, 'rentapp/insertar_foto.html', {'renta_title':renta_title,'renta_id':renta_id,'datos_fotos': datos_fotos, 'form': form})

@login_required
def insertar_renta(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RentaForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            provincia_nombre = form.cleaned_data['provincia'].split('.')
            municipio_nombre =  form.cleaned_data['municipio'].split('.')
            #num_calle = form.cleaned_data['direccion']
            #direccion_full = f"{form.cleaned_data['direccion']}, {form.cleaned_data['sector']}, DO."
            direccion_full = f"{form.cleaned_data['direccion']}, {form.cleaned_data['sector']}, {municipio_nombre[1]}, {provincia_nombre[1]}, República Dominicana"
            # geolocator = Nominatim(user_agent="rentapp", timeout=10)
            # location = geolocator.geocode(direccion_full)
            # location = ""

            # process the data in form.cleaned_data as required
            # ...
            new_renta = Renta(
                user = form.cleaned_data['user'],
                direccion = direccion_full,
                sector = form.cleaned_data['sector'],
                municipio = municipio_nombre[1],
                provincia = provincia_nombre[1],
                referencia = form.cleaned_data['referencia'],
                # pub_date = time.strftime('%Y-%m-%d %I:%M'),
                )
            new_renta.save()
            obj = Renta.objects.latest('id')
            renta_id = obj

            # renta_direccion = obj.direccion
            # obj = Amistad.objects.latest('id')

            # redirect to a new URL:
            return HttpResponseRedirect(f'/insertar_foto/{renta_id.id}')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = RentaForm()
    return render(request, 'rentapp/insertar_renta.html', {'form': form})

def index(request):
    rentas = list(Renta.objects.all().order_by('-id'))
    fotos_rentas = list(Foto.objects.all().values().order_by('-id'))
    # fotos_rentas = list(Foto.objects.all().select_related('renta').values(
    #     'renta__usertario', 'renta__id', 'renta__direccion',
    #     'id', 'image_renta', 'name_foto_renta').order_by('-id'))
    p = Paginator(rentas, 4)
    page = request.GET.get('page')
    rentas = p.get_page(page)

    context = {
        "fotos_rentas":fotos_rentas,
        "rentas": rentas,
    }
    return render(request, "rentapp/index.html", context)
@login_required
def detail(request, renta_id):

    try:
        fotos = Foto.objects.filter(renta=renta_id)
        renta_location = Renta.objects.get(pk=renta_id)
        # geolocator = Nominatim(user_agent="rentapp", timeout=10)
        # location = geolocator.geocode(renta_location.direccion)
        location = ""

    except Exception as e:
       return HttpResponse(f'ahora si :{e}' )
    context = {
            "fotos" : fotos,
            "location" : location,
            "renta_location" : renta_location,
        }
    return render(request, "rentapp/detail.html", context)

# Reparar
def buscar(request):
    # br = Renta.objects.all()
    if 'buscar' in request.method:
        b = request.post(request, "buscar")
        q_rentas = Renta.objects.filter(direccion__search = b)
    else:
        q_rentas = Renta.objects.all().order_by('-id')
        p = Paginator(q_rentas, 5)
        page = request.GET.get("page")
        rentas = p.get_page(page)
        context = {
        "rentas" : rentas,
        "fotos" : list(Foto.objects.values()),
        }
        response = render(request, "rentapp/buscar.html", context )
        return response

def quien_es():
    pass

@login_required
def dashboard(request, id_user):
    quien_es = User.objects.all().filter(id=id_user).values("phone_number")[0]['phone_number']
    # tener todas las rentas del usuario
    rentas = Renta.objects.all().filter(user=id_user).order_by('-id')
    # user_app = User.objects.all().filter(usertario=id_rendatario).order_by('-id')
    print(quien_es)
    print(rentas)
    context = {
        "quien_es": quien_es,
        "rentas": rentas,
    }
    return render(request, "rentapp/dashboard.html", context)

def delete_renta(request, id_renta, user):
    renta = Renta.objects.filter(id=id_renta)
    renta.delete()
    return HttpResponseRedirect(f"../dashboard/{user}")


def prueba(request):

    # amistad_userdador = Amistad.objects.filter(userdador = userdador_id).select_related('renta','usertario','userdador').values(
    #     'renta', 'userdador', 'usertario').order_by('-id')    # id, mensaje, pub_date, relacion, userdador, userdador_id, usertario, usertario_id
    # # amistad = Amistad.objects.filter(userdador=userdador_id).values("id", 'pub_date', 'relacion', 'userdador', 'usertario',)
    rentas = list(Renta.objects.all().values())
    fotos_rentas = list(Foto.objects.all().values())

    return  HttpResponse(f"rentas: {rentas}----Fotos:{fotos_rentas}" )

