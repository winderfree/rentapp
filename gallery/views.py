from django.shortcuts import render
from . models import *
from . forms import *
from django.http import HttpResponseRedirect

def image_gallery(request):
    images = Image.objects.all().order_by('-id')[:3]
    print(images)
    return render(request, 'image_gallery.html', {'images' : images})

def upload_image(request):
    if request.method == 'GET':
        return render(request, 'upload_image.html')
    elif request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            new_image = Image(
                image = form.cleaned_data['image'], 
                name = form.cleaned_data['name'])
            new_image.save()
            return HttpResponseRedirect('/gallery/upload_image/')