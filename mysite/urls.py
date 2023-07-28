from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('rentapp/', include('rentapp.urls')),
    path('gallery/', include('gallery.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
