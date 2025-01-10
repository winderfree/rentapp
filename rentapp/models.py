from django.db import models
from django.contrib.auth.models import AbstractUser

from mysite import settings

class User(AbstractUser): 
    
    categoria = models.CharField(
        max_length=24,
    # default = "propietario",
    )  

    def __str__(self):
        return f'{self.username}'
    
  
    def get_categoria(self):
        return self.categoria
 
class Renta(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    direccion = models.CharField(max_length=200)
    provincia = models.CharField(max_length=200, blank=True)
    municipio = models.CharField(max_length=200, blank=True)
    sector = models.CharField(max_length=200, blank=True)
    referencia = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.direccion

class Amistad(models.Model):
    renta = models.ForeignKey(Renta, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    relacion = models.CharField(max_length=200, null=True)
    pub_date = models.DateTimeField("fecha publicado", null=True)

    def __str__(self):
        return f'{self.id}'
    # slug = models.SlugField(editable=False)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

class Mensaje(models.Model):
    amistad = models.ForeignKey(Amistad, on_delete=models.CASCADE)
    texto = models.CharField(max_length=250)
    tipo = models.CharField(max_length=24, null=True )
    pub_date = models.DateTimeField("fecha publicado", null=True)
    
    def __str__(self):
        return f"{self.amistad}"
      
class Foto(models.Model):
    renta = models.ForeignKey(Renta, on_delete=models.CASCADE)
    image_renta = models.ImageField(upload_to='gallery', default='gallery/static/images/no-img.jpg')
    name_foto_renta = models.CharField(max_length=200)

    def __str__(self):
        return f'self.id'