from django.urls import path

from . import views


app_name = 'todo'
urlpatterns = [
    path("", views.home, name="home"),
    path("tasks/", views.TaskList.as_view(), name="tasks"),
    path("tasks/<int:pk>/", views.TaskDetail.as_view(), name="task_detail"),
    path("tasks/create/", views.TaskCreate.as_view(), name="task_create"),
    path("tasks/<int:pk>/update/", views.TaskUpdate.as_view(), name="task_update"),
    path("task/<int:pk>/delete/", views.TaskDelete.as_view(), name="task_delete"),
]