from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib import messages
from django.shortcuts import render, redirect

from . import forms 


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
    form_class = forms.SignupForm
    success_url = reverse_lazy('todo:tasks')
    redirect_authenticated_user = True
    
    def form_valid(self, form):
        user = form.save()
        
        if user:
            login(self.request, user)
        
        return super().form_valid(form)


class MyProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user_form = forms.UserUpdateForm(instance=request.user)
        profile_form = forms.ProfileUpdateForm(instance=request.user.profile)
        
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        
        return render(request, 'users/profile.html', context=context)
    
    def post(self, request):
        user_form = forms.UserUpdateForm(request.POST, instance=request.user)
        profile_form = forms.ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            
            messages.add_message(request, messages.SUCCESS, 'Your profile has been updated!')
            
            return redirect('users:profile')
        else:
            context = {
                'user_form': user_form,
                'profile_form': profile_form
            }
            
            messages.add_message(request, messages.ERROR, 'Error updating your profile')
        
            return render(request, 'users/profile.html', context=context)
    