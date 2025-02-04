from django.urls import path
from .views import TaskListCreateAPIView, TaskDetailAPIView

urlpatterns = [
    path("tasks/", TaskListCreateAPIView.as_view(), name="api-task-list"),
    path("tasks/<int:task_id>/", TaskDetailAPIView.as_view(), name="api-task-detail"),
]
