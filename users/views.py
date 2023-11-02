from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages


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