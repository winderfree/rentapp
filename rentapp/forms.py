from django import forms
from . models import *

class RentaForm(forms.ModelForm):
    class Meta:
        model = Renta
        fields = ['id', 'direccion', 'referencia', 'e_mail', 'telefono']
