from django.shortcuts import render
from django.views import generic

from .models import Task

# Create your views here.
def home(request):
    return render(request, 'home.html')


class TaskList(generic.ListView):
    model = Task
    context_object_name = 'tasks'