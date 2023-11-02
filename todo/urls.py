from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("tasks/", views.TaskList.as_view(), name="tasks"),
    path("tasks/<int:pk>/", views.TaskDetail.as_view(), name="task_detail"),
]