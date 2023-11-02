from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Task

# Create your views here.
def home(request):
    return render(request, 'home.html')


class TaskList(generic.ListView):
    model = Task
    context_object_name = 'tasks'


class TaskDetail(generic.DetailView):
    model = Task
    context_object_name = 'task'


class TaskCreate(generic.CreateView):
    model = Task
    fields = ['title', 'description']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        messages.add_message(self.request, messages.SUCCESS, 'Task created!')
        return super().form_valid(form)


class TaskUpdate(generic.UpdateView):
    model = Task
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.add_message(self.request, messages.SUCCESS, 'Task updated!')
        return super().form_valid(form)