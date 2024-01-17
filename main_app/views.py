from django.shortcuts import render
#importing class based views(CBVs)
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Cat

# Add this cats list below the imports
'''
cats = [
  {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
  {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
  {'name': 'Cookie', 'breed': 'calico', 'description': 'scary', 'age': 1},
]
'''

#Create your views here.
#render page based on request
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

#show all cats
def cats_index(request):
    #obs from db, uses the model, calls all, print all
    cats = Cat.objects.all()

    for cat in cats:
        print(cat)
    #pass data in views
    return render(request, 'cats/index.html', {'cats': cats})

#detail view - shows one cat at 'cat/:id'
def cats_detail(request, cat_id):
    #find one cat with its id
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', {'cat': cat})

#inherit from the CBV - CreateView to make our cats create view
class CatCreate(CreateView):
    #tell the createview to use the cat model for all its functionality
    model = Cat
    #this view creates a form so we need to identify which fields to use
    fields = '__all__'
    #we can add other options inside this view 

#Update view
    class CatUpdate(UpdateView):
        model = Cat

    #don't allow name to be renamed
    fields = ['breed', 'descriptions', 'age']

#Delete View
class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats'