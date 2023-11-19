import datetime
from django import forms
from .models import *

class RentaForm(forms.ModelForm):
    class Meta:
        model = Renta
        fields = ['usertario', 'direccion', 'sector', 'municipio', 'provincia', 'referencia']
        # fields = "__all__"
        widgets = {
            
            'usertario': forms.Select(attrs={'style':'margin:10px 10px 10px 0px;','class':'form-control '}),
            'direccion': forms.TextInput(attrs={'style':'margin:10px 10px 10px 0px;', 'class':'form-control ','placeholder': 'ex: 23, nombre Calle...'}),
            'referencia': forms.TextInput(attrs={'style':'margin:10px 10px 10px 0px;','class':'form-control ','placeholder': 'ex: Lugar de referencia...'}),
            'provincia': forms.Select(attrs={'class':'form-control '}),
            'municipio': forms.Select(attrs={'class':'form-control '}),
            'sector': forms.Select(attrs={'class':'form-control '}),
            
            }
        labels = {
            'usertario': 'Rendataurio',
        }
class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['amistad', 'texto']
        widgets = {
            
            'amistad': forms.Select(attrs={'style':'margin:10px 10px 10px 0px;','class':'form-control'}),
            'texto': forms.TextInput(attrs={'style':'margin:10px 10px 10px 0px;','class':'form-control','placeholder': 'ex: Mensaje...'}),
           
            }

class AmistadForm(forms.ModelForm):
    class Meta:
        model = Amistad
        fields = ['usertario', 'userdador', 'relacion']
        widgets = {
            'relacion': forms.TextInput(attrs={'style':'margin:10px 10px 10px 0px;','class':'form-control ','placeholder': 'ex: Interes por Articulo.'}),
            'usertario': forms.Select(attrs={'style':'margin:10px 10px 10px 0px;','class':'form-control '}),
            'userdador': forms.Select(attrs={'style':'margin:10px 10px 10px 0px;','class':'form-control '}),
        }

class UsertarioForm(forms.ModelForm):
    class Meta:
        model = Usertario
        fields = ('username', 'password', 'email', 'groups')
        
class UserdadorForm(forms.ModelForm):
    class Meta:
        model = Userdador
        fields = "__all__"
        #fields = ['e_mail', 'telefono', 'password']

        widgets = {
            'e_mail': forms.TextInput(attrs={'style':'margin:10px 10px 10px 0px;','class':'form-control  bi-envelope','placeholder': 'Inserte su E-mail'}),
            'telefono': forms.TextInput(attrs={'style':'margin:10px 10px 10px 0px;','class':'form-control ','placeholder': 'Ex: 809 - 555 - 5555'}),
            'password': forms.TextInput(attrs={'style':'margin:10px 10px 10px 0px;','class':'form-control ','placeholder': 'Nuevo Password'}),
        }

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

    