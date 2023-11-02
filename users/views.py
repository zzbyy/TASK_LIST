from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages

from .forms import SignupForm


class MyLoginView(LoginView):
    # The template_name of LoginView defaults to 'registration/login.html'. 
    # So here we need to set it to 'users/login.html'
    template_name = 'users/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('todo:tasks') 
    
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))


class SignupView(generic.FormView):
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('todo:tasks')
    redirect_authenticated_user = True
    
    def form_valid(self, form):
        user = form.save()
        
        if user:
            login(self.request, user)
        
        return super().form_valid(form)