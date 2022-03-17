from django.views.generic import ListView
from .models import ToDoList


# the ListListView class will display a list of the to-do list titles
class ListListView(ListView):
    model = ToDoList
    template_name = "todo_app/index.html"
