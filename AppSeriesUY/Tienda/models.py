from django.db import models
from django.utils import timezone
from django.urls import reverse

class Ventas(models.Model):
    nombre = models.CharField(max_length=100)
    vendedor = models.CharField(max_length=100, default='Autor')
    descripcion = models.TextField()
    pub_date = models.DateTimeField('date published', default=timezone.now)
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to='feed_images', blank=True, null=True)
    def get_absolute_url(self):
        return reverse('venta_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.nombre
