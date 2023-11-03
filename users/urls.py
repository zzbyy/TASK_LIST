from django.urls import path
from django.contrib.auth.views import (
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.urls import reverse_lazy

from . import views
 
app_name = 'users'
urlpatterns = [
    path('login/', views.MyLoginView.as_view(redirect_authenticated_user=True), name='login'),
    
    path('logout/', LogoutView.as_view(next_page='users:login'), name='logout'),
    
    path('signup/', views.SignupView.as_view(), name='signup'),
    
    path('password_reset/', 
         PasswordResetView.as_view(template_name='users/password_reset.html', email_template_name='users/password_reset_email.html', success_url=reverse_lazy('users:password_reset_done')), 
         name='password_reset'),
    
    path('password_reset/done/', 
         PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), 
         name='password_reset_done'),
    
    path('password_reset_confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html', success_url=reverse_lazy("users:password_reset_complete")), 
         name='password_reset_confirm'),
    
    path('password_reset/complete/', 
         PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), 
         name='password_reset_complete'),
    
    path('profile/', views.MyProfileView.as_view(), name='profile'),
]
