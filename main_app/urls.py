from django.urls import path
from . import views

#create the routes, render views html, name it
urlpatterns=[
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    #route for index page of cats
    path('cats/', views.cats_index, name='index'),
    #route for the detail page of our cats
    path('cats/<int:cat_id>', views.cats_detail, name ='detail'),
    path('cats/create', views.CatCreate.as_view(), name = 'cats_create'),
    path('cats/<int:pk>/update', views.CatUpdate.as_view(), name = 'cats_update')
]