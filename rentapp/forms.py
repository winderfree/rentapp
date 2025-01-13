import datetime
from django import forms
from .models import *


class RentaForm(forms.ModelForm):
    class Meta:
        model = Renta
        fields = ['user', 'direccion', 'sector', 'municipio', 'provincia', 'referencia']
        # fields = "__all__"
        # widgets = {
            
        #     'user': forms.Select(attrs={'style':'margin:10px 10px 10px 0px;','class':'form-control '}),
        #     'direccion': forms.TextInput(attrs={'style':'margin:10px 10px 10px 0px;', 'class':'form-control ','placeholder': 'ex: 23, nombre Calle...'}),
        #     'referencia': forms.TextInput(attrs={'style':'margin:10px 10px 10px 0px;','class':'form-control ','placeholder': 'ex: Lugar de referencia...'}),
        #     'provincia': forms.Select(attrs={'class':'form-control '}),
        #     'municipio': forms.Select(attrs={'class':'form-control '}),
        #     'sector': forms.Select(attrs={'class':'form-control '}),
            
        #     }
        # labels = {
        #     'user': 'Usuario',
        # }
class FotoForm(forms.ModelForm):
    class Meta:
        model = Foto
        # fields = "__all__"
        fields = ['renta', 'image_renta', 'name_foto_renta']
        widgets = {
            'renta': forms.Select(attrs={'style':'margin:10px 10px 10px 0px;','class':'form-control '}),
            'image_renta': forms.FileInput(attrs={'title':'Asd','style':'margin:10px 0px 10px 10px;','class':'form-control form-control-md '}),
            'name_foto_renta': forms.TextInput(attrs={'style':'margin:10px 10px 10px 0px;','class':'form-control ', 'placeholder': 'ex: Descripción Foto.'}),
        }
        labels = {
            'name_foto_renta': 'Descripción',
            'image_renta': 'Select'
        }

class RentaForm(forms.ModelForm):
    class Meta:
        model = Renta
        fields = '__all__'
        

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username', 'email', 'password', 'phone_number']
