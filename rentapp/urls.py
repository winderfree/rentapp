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
    # ex: /rentapp/insertar_renta/
    path('insertar_renta/', views.insertar_renta, name='insertar_renta'),
    # ex: /rentapp/insertar_foto/
    path('insertar_foto/', views.insertar_foto, name='insertar_foto'),
    # ex: /rentapp/insertar_userdador/
    path('insertar_userdador/', views.insertar_userdador, name='insertar_userdador'),
    # ex: /rentapp/insertar_usertario/
    path('insertar_usertario/', views.insertar_usertario, name='insertar_usertario'),
    # ex: /rentapp/insertar_amistad/
    path('insertar_amistad/', views.insertar_amistad, name='insertar_amistad'),
    # ex: /rentapp/insertar_mensaje/
    path('insertar_mensaje/', views.insertar_mensaje, name='insertar_mensaje'),
    # ex: /rentapp/insertar_mensaje_rendatario/
    path('insertar_mensaje_rendatario/', views.insertar_mensaje_rendatario, name='insertar_mensaje_rendatario'),
    # logout_user
    path('/', views.logout_user, name='logout_user'),
    # probando
    path('prueba_jquery/', views.prueba_jquery, name='prueba_jquery'),
    # Nothing yet!
    path('image_rentapp/', views.image_rentapp, name='image_rentapp'),
    path('upload_image/', views.upload_image, name='upload_image'),

]