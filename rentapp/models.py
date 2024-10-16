from django.db import models
from django.contrib.auth.models import User

class Usertario(User, models.Model):    
    class Meta:
        db_table = "Usertario"
    
    tipo = models.CharField(max_length=24, null=True )
    categoria = models.CharField(
        max_length=24,
        # default = "propietario",
    )
    def __str__(self):
        return f'{self.username}-{self.categoria}'
    
class Userdador(User, models.Model):
    class Meta:
        db_table = "Userdador"

    tipo = models.CharField(max_length=24, null=True )    
    def __str__(self):
        return f'{self.username}'

class Renta(models.Model):
    usertario = models.ForeignKey(Usertario, on_delete=models.CASCADE, null=True)
    direccion = models.CharField(max_length=200)
    provincia = models.CharField(max_length=200, blank=True)
    municipio = models.CharField(max_length=200, blank=True)
    sector = models.CharField(max_length=200, blank=True)

    referencia = models.CharField(max_length=200)
    pub_date = models.DateTimeField("fecha publicado")
    latitud = models.CharField(max_length=42, blank=True)
    longitud = models.CharField(max_length=42, blank=True)

    # q = Question(question_text="What's new?", pub_date=timezone.now())
    def __str__(self):
        return f'{int(self.id)}'

class Amistad(models.Model):
    renta = models.ForeignKey(Renta, on_delete=models.CASCADE, null=True)
    usertario = models.ForeignKey(Usertario, on_delete=models.CASCADE)
    userdador = models.ForeignKey(Userdador, on_delete=models.CASCADE)
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