from django.urls import path
from .views import MyLoginView
from django.contrib.auth.views import LogoutView
 
app_name = 'users'
urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
