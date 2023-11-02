from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views
 
app_name = 'users'
urlpatterns = [
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='users:login'), name='logout'),
    path('signup/', views.SignupView.as_view(), name='signup'),
]
