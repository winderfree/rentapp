from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("New Fields", {'fields': ('tipo', 'categoria')}),
    )
    # list_display = ['username', 'email', 'tipo', 'categoria']

admin.site.register(Amistad)
admin.site.register(Mensaje)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Renta)
admin.site.register(Foto)

