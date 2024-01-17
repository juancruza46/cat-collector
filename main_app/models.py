from django.db import models
from django.urls import reverse

# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    age = models.IntegerField()
    #will display name instead of "objects" in admin
    def __str__(self):
        return self.name
    
    #this is the get_absolute_url method, it redirects to the detail page where appropriate
    def get_absolute_url(self):
        return reverse('detail', kwargs={'cat_id': self.id})


