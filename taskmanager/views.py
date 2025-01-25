from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.
class TaskListView(TemplateView):
    template_name = "pages/task-list.html"
