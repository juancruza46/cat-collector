from django.contrib import admin

#import cat model
from .models import Cat

# Register your models here.
admin.site.register(Cat)