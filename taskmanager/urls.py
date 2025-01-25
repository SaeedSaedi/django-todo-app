from django.urls import include, path
from . import views
from django.views.generic import TemplateView

app_name = "taskmanager"

urlpatterns = [
    path("list/", views.TaskListView.as_view(), name="task-list"),
]
