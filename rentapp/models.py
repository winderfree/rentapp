from django.db import models

class Renta(models.Model):
    direccion = models.CharField(max_length=200)
    referencia = models.CharField(max_length=200)
    e_mail = models.EmailField(max_length=254)
    telefono =  models.CharField(max_length=50)
    pub_date = models.DateTimeField("fecha publicado")
    latitud = models.CharField(max_length=24)
    longitud = models.CharField(max_length=24)

    # q = Question(question_text="What's new?", pub_date=timezone.now())
    def __str__(self):
        return self.direccion
    
class Fotos(models.Model):
    renta = models.ForeignKey(Renta, on_delete=models.CASCADE)
    image_renta = models.ImageField(upload_to='rentapp', default='gallery/static/images/no-img.jpg')
    name_foto_renta = models.CharField(max_length=200)

    def __str__(self):
        return self.name_foto_renta