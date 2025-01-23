from django.db import models
from django.utils import timezone
from django.urls import reverse

class Posts(models.Model):
    title = models.CharField(max_length=100)
    autor = models.CharField(max_length=100, default='Autor')
    description = models.TextField()
    pub_date = models.DateTimeField('date published', default=timezone.now)
    link = models.URLField()
    image = models.ImageField(upload_to='feed_images', blank=True, null=True)
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
