from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Task
import json
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


# Task Create View
@method_decorator(csrf_exempt, name="dispatch")
@method_decorator(login_required, name="dispatch")
class TaskCreateView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            title = data.get("title")
            status = data.get("status", 0)
            task = Task.objects.create(user=request.user, title=title, status=status)
            return JsonResponse({"success": True, "task_id": task.id})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})


# Task Delete View
@method_decorator(csrf_exempt, name="dispatch")
@method_decorator(login_required, name="dispatch")
class TaskDeleteView(View):
    def delete(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id, user=request.user)
            task.delete()
            return JsonResponse({"success": True})
        except Task.DoesNotExist:
            return JsonResponse({"success": False, "error": "Task not found"})


# Task Update View
@method_decorator(csrf_exempt, name="dispatch")
@method_decorator(login_required, name="dispatch")
class TaskUpdateView(View):
    def put(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id, user=request.user)
            data = json.loads(request.body)
            if "title" in data:
                task.title = data["title"]
            if "status" in data:
                task.status = data["status"]
            task.save()
            return JsonResponse({"success": True})
        except Task.DoesNotExist:
            return JsonResponse({"success": False, "error": "Task not found"})


# Task List View
class TaskListView(TemplateView):
    template_name = "pages/task-list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks_todo"] = Task.objects.filter(user=self.request.user, status=0)
        context["tasks_doing"] = Task.objects.filter(user=self.request.user, status=1)
        context["tasks_done"] = Task.objects.filter(user=self.request.user, status=2)
        return context
