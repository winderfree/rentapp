import time
from asgiref.sync import sync_to_async
import asyncio
from django.core.paginator import Paginator
from geopy.geocoders import Nominatim
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/rentapp')

def prueba_jquery(request):
    datos_amistad = list(Amistad.objects.values().order_by("-id"))
    datos = list(Mensaje.objects.values().order_by("-id"))
    return render(request, 'rentapp/prueba_jquery.html', {'datos': datos, 'datos_amistad':datos_amistad })
   

def insertar_mensaje(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MensajeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            new_mensaje = Mensaje(
                amistad = form.cleaned_data['amistad'], 
                texto = form.cleaned_data['texto'],
                tipo = 'rendador',
                pub_date = time.strftime('%Y-%m-%d %I:%M')
                 )
            new_mensaje.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/rentapp/insertar_mensaje/')
    # if a GET (or any other method) we'll create a blank form
    else:
        datos_amistad = list(Amistad.objects.values().order_by("-id"))
        datos = list(Mensaje.objects.values().order_by("-id"))
        # print (datos)
        form = MensajeForm()
    return render(request, 'rentapp/insertar_mensaje.html', {'form': form, 'datos': datos, 'datos_amistad': datos_amistad })

   
def insertar_mensaje_rendatario(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MensajeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            new_mensaje = Mensaje(
                amistad = form.cleaned_data['amistad'], 
                texto = form.cleaned_data['texto'],
                tipo = 'rendatario',
                pub_date = time.strftime('%Y-%m-%d %I:%M')
                 )
            new_mensaje.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/rentapp/insertar_mensaje_rendatario/')
    # if a GET (or any other method) we'll create a blank form
    else:
        datos_amistad = list(Amistad.objects.values().order_by("-id"))
        datos = list(Mensaje.objects.values().order_by("-id"))
        # print (datos)
        form = MensajeForm()
    return render(request, 'rentapp/insertar_mensaje_rendatario.html', {'form': form, 'datos': datos, 'datos_amistad': datos_amistad })


def insertar_amistad(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AmistadForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            new_amistad = Amistad(
                usertario = form.cleaned_data['usertario'], 
                userdador = form.cleaned_data['userdador'],
                relacion = form.cleaned_data['relacion'],                
                pub_date = time.strftime('%Y-%m-%d %I:%M') ) 
            new_amistad.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/rentapp/insertar_mensaje/')
    # if a GET (or any other method) we'll create a blank form
    else:
        datos = list(Amistad.objects.values().order_by("-id"))
        # print (datos)
        form = AmistadForm()
    return render(request, 'rentapp/insertar_amistad.html', {'form': form, 'datos': datos, })

from django.contrib.auth.hashers import make_password

def insertar_usertario(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UsertarioForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            user = form.save(commit=False)

            username = form.cleaned_data['username'] 
            password = form.cleaned_data['password']
            groups = form.cleaned_data['groups']
            email = form.cleaned_data['email']
            #  Use set_password here
            user.set_password(password)

            user.save()

            # redirect to a new URL:
            return HttpResponseRedirect('/rentapp/insertar_renta/')
    # if a GET (or any other method) we'll create a blank form
    else:
        #datos = list(Usertario.objects.values().order_by("-id"))
        form = UsertarioForm()
    return render(request, 'rentapp/insertar_usertario.html', {'form': form})

def insertar_userdador(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserdadorForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            new_userdador = Userdador(
                e_mail = form.cleaned_data['e_mail'], 
                telefono = form.cleaned_data['telefono'],
                password = form.cleaned_data['password'])
            new_userdador.save()
            # redirect to a new URL:
            return HttpResponseRedirect('../../rentapp/insertar_userdador')
    # if a GET (or any other method) we'll create a blank form
    else:    
        datos = list(Userdador.objects.values().order_by("-id"))
        # print (datos)
        form = UserdadorForm()
    return render(request, 'rentapp/insertar_userdador.html', {'form': form, 'datos': datos, })

#async_function = sync_to_async(sync_function, thread_sensitive=False)
@login_required    
def insertar_foto(request):
    
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
            # redirect to a new URL:
            return HttpResponseRedirect('/rentapp/insertar_foto/')
    # if a GET (or any other method) we'll create a blank form
    else:
        datos_fotos = list(Foto.objects.values().order_by("-id"))
        form = FotoForm()
    return render(request, 'rentapp/insertar_foto.html', {'datos_fotos': datos_fotos, 'form': form})

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
            geolocator = Nominatim(user_agent="rentapp", timeout=10)
            location = geolocator.geocode(direccion_full)        

            # process the data in form.cleaned_data as required
            # ...
            new_renta = Renta(
                usertario = form.cleaned_data['usertario'], 
                direccion = direccion_full,
                sector = form.cleaned_data['sector'], 
                municipio = municipio_nombre[1], 
                provincia = provincia_nombre[1],
                referencia = form.cleaned_data['referencia'],
                pub_date = time.strftime('%Y-%m-%d %I:%M'),
                latitud = location.latitude if location else 'not' ,
                longitud = location.longitude if location else 'not' )
            new_renta.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/rentapp/insertar_foto/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = RentaForm()
    return render(request, 'rentapp/insertar_renta.html', {'form': form})

def index(request):
    p = Paginator(Renta.objects.values().order_by("-id"), 4)
    page = request.GET.get('page')
    rentas = p.get_page(page)

    context = {
        "rentas": rentas,
        "fotos": list(Foto.objects.values()),
        'latest_renta_list' : list(Renta.objects.values()),
    }
    return render(request, "rentapp/index.html", context)
@login_required
def detail(request, renta_id):
    
    try:
        fotos = Foto.objects.filter(renta=renta_id)
        renta_location = Renta.objects.get(pk=renta_id)
        geolocator = Nominatim(user_agent="rentapp", timeout=10)
        location = geolocator.geocode(renta_location.direccion)        
        
    except Exception as e:
       return HttpResponse(f'ahora si :{e}' )
    context = {
            "fotos" : fotos,
            "location" : location,
            "renta_location" : renta_location,
        }
    return render(request, "rentapp/detail.html", context)
# darle sentido al buscador
def buscar(request):
    fotos = Foto.objects.all().select_related('renta')
    if 'buscar' in request.POST:
        b = request.POST["buscar"]
        q_rentas = Renta.objects.filter(direccion__contains = b)
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

def image_rentapp(request):
    images = Renta.objects.all().order_by('-id')[:3]
    print(images)
    return render(request, 'image_gallery.html', {'images' : images})

def upload_image(request):
    if request.method == 'GET':
        return render(request, 'upload_image.html')
    elif request.method == 'POST':
        form = RentaForm(request.POST, request.FILES)
        if form.is_valid():
            new_image = Foto(
                image = form.cleaned_data['image'], 
                name = form.cleaned_data['name'])
            new_image.save()
            return HttpResponseRedirect('/rentapp/upload_image/')

