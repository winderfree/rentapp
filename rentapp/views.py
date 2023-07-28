from django.core.paginator import Paginator
from geopy.geocoders import Nominatim
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
# from django.template import loader
from . forms import *

from .models import Renta, Fotos

def index(request):
   # fotos_rentas = list(Fotos.objects.all().select_related('renta'))
   # template = loader.get_template("rentapp/index.html")
    p = Paginator(Renta.objects.values().order_by("-pub_date"), 3)
    page = request.GET.get('page')
    rentas = p.get_page(page)

    context = {
       # "fotos_rentas": fotos_rentas,
        "rentas": rentas,
        "fotos": list(Fotos.objects.values()),
        'latest_renta_list' : list(Renta.objects.values()),
    }
    return render(request, "rentapp/index.html", context)
    # return HttpResponse(template.render(context, request))
    # output = ", ".join([q.direccion for q in latest_renta_list])
    # return HttpResponse(output)

def detail(request, renta_id):
    
    try:
        fotos = Fotos.objects.filter(renta=renta_id)
        renta_location = Renta.objects.get(pk=renta_id)
        geolocator = Nominatim(user_agent="rentapp", timeout=10)
        location = geolocator.geocode(renta_location.direccion)        
        #renta = Renta.objects.get(pk=renta_id)
        
    except Exception as e:
       return HttpResponse(f'ahora si :{e}' )
    context = {
            "fotos" : fotos,
            #"renta" : renta,
            "location" : location,
            "renta_location" : renta_location,
        }
    return render(request, "rentapp/detail.html", context)

def buscar(request):
    fotos = Fotos.objects.all().select_related('renta')
    if 'buscar' in request.POST:
        b = request.POST["buscar"]
        q_rentas = Renta.objects.filter(direccion__contains = b)
    else:
        q_rentas = Renta.objects.all().order_by('-id')        
    p = Paginator(q_rentas, 5)  # Show 2 contacts per page.
    #p = Paginator(Renta.objects.filter(direccion__contains = request.POST["buscar"] ), 2)  # Show 2 contacts per page.
    #page = request.GET.get("page")
    #rentas = p.get_page(page)
    # if request.method == 'POST':
    page = request.GET.get("page")
    rentas = p.get_page(page)
    #direccion = Renta.objects.filter(direccion__contains = request.POST["buscar"] )    
    #direcciones = p.get_page(page_obj)
    context = {
    "rentas" : rentas,
    "fotos" : list(Fotos.objects.values()),
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
            new_image = Fotos(
                image = form.cleaned_data['image'], 
                name = form.cleaned_data['name'])
            new_image.save()
            return HttpResponseRedirect('/rentapp/upload_image/')

