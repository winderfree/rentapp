from django.db import models

class Mensaje(models.Model):
    
    amistad_id = models.IntegerField(null=True, blank=True)
    texto =  models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.texto}, {self.amistad_id}"
