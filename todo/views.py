from typing import Any
from django.db import models
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task

# Create your views here.
def home(request):
    return render(request, 'home.html')


class TaskList(LoginRequiredMixin, generic.ListView):
    model = Task
    context_object_name = 'tasks'
    
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class TaskDetail(LoginRequiredMixin, generic.DetailView):
    model = Task
    context_object_name = 'task'
    
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class TaskCreate(LoginRequiredMixin, generic.CreateView):
    model = Task
    fields = ['title', 'description']
    success_url = reverse_lazy('todo:tasks')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        messages.add_message(self.request, messages.SUCCESS, 'Task created!')
        return super().form_valid(form)
    
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class TaskUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Task
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('todo:tasks')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.add_message(self.request, messages.SUCCESS, 'Task updated!')
        return super().form_valid(form)
    
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class TaskDelete(LoginRequiredMixin, generic.DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('todo:tasks')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.add_message(self.request, messages.SUCCESS, 'Task deleted!')
        return super().form_valid(form)
    
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)