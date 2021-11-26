from django.shortcuts import render
from .models import Item

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

