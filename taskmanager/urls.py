from django.urls import path
from .views import TaskCreateView, TaskDeleteView, TaskUpdateView, TaskListView

app_name = "taskmanager"

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/delete/<int:task_id>/", TaskDeleteView.as_view(), name="task-delete"),
    path("task/update/<int:task_id>/", TaskUpdateView.as_view(), name="task-update"),
]
