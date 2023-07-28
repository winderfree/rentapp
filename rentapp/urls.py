from django.urls import path
from . import views

app_name = 'rentapp'

urlpatterns = [
    # ex: /rentapp/
    path('', views.index, name='index'),
    # ex: /rentapp/2/
    path('<int:renta_id>/', views.detail, name='detail'),
    # ex: /rentapp/"direccion"/
    path('buscar/', views.buscar, name='buscar'),
    path('image_rentapp/', views.image_rentapp, name='image_rentapp'),
    path('upload_image/', views.upload_image, name='upload_image'),
]