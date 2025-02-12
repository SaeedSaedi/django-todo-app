from celery import shared_task
from .models import Task


@shared_task
def delete_completed_tasks():
    Task.objects.filter(status=2).delete()
    return "Completed tasks deleted"
