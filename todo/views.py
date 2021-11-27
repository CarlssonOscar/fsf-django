from django.shortcuts import render, redirect
from .models import Item
# Observera att detta är en class från forms.py
from .forms import ItemForm

# Create your views here.
# - Ensures ensure that we have access to it in our todo list .html
#  template. Once we save this we've got everything we need 
# to ensure complete communication. Between the users of
# our app on the front end. And our database on the back end.


def get_todo_list(request):
    # Query set of all items in the database
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    # Add item form (POST request), observera att redirect behövde importeras (rad 1).
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    # Går nu att {{ form }} i html
    form = ItemForm
    context = {
    'form': form
    }
    # GET request.    
    return render(request, 'todo/add_item.html', context)


def edit_item(request, item_id):
    return render(request, 'todo/edit_item')