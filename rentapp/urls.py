from django.urls import path
from . import views

app_name = 'rentapp'

urlpatterns = [
    # insertar User
    path('insertar_user/', views.insertar_user, name='insertar_user' ),
    # prueba url
    path('prueba/', views.prueba, name='prueba'),
    # ex: /rentapp/
    path('', views.index, name='index'),
    # ex: /rentapp/2/
    path('<int:renta_id>', views.detail, name='detail'),
    # ex: /rentapp/"direccion"/
    path('buscar/', views.buscar, name='buscar'),
    # ex: /rentapp/insertar_renta/
    path('insertar_renta/', views.insertar_renta, name='insertar_renta'),
    # ex: /rentapp/insertar_foto/
    path('insertar_foto/<int:renta_id>', views.insertar_foto, name='insertar_foto'),

    # ex: /rentapp/dashboard usertario
    path('dashboard/<int:id_user>', views.dashboard, name='dashboard'),
    # ex: /rentapp/dashboard userdador
   
    path('delete_renta/<int:id_renta>-<int:user>', views.delete_renta, name='delete_renta' ),
    # logout_user
    path(' ', views.logout_user, name='logout_user'),
    # login
    # path(' ', views.login_user, name='login_user'),

    # Nothing yet!
    # path('image_rentapp/', views.image_rentapp, name='image_rentapp'),
    # path('upload_image/', views.upload_image, name='upload_image'),

]