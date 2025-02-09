import pytest
import json
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from ..models import Task

User = get_user_model()


@pytest.mark.django_db
def test_task_create_view(client):
    user = User.objects.create_user(username="test@example.com", password="securepass")
    client.login(username="test@example.com", password="securepass")

    data = {"title": "New Task", "status": 0}

    response = client.post(
        reverse("taskmanager:task-create"),
        json.dumps(data),
        content_type="application/json",
    )

    assert response.status_code == 200
    response_data = response.json()
    assert response_data["success"] is True
    assert "task_id" in response_data  # Check that a task ID is returned

    # Verify task was created in the database
    assert Task.objects.filter(id=response_data["task_id"]).exists()


@pytest.mark.django_db
def test_task_delete_view(client):
    user = User.objects.create_user(username="test@example.com", password="securepass")
    client.login(username="test@example.com", password="securepass")

    # Create a task to delete
    task = Task.objects.create(user=user, title="Task to delete", status=0)

    # Send delete request
    response = client.delete(reverse("taskmanager:task-delete", args=[task.id]))

    assert response.status_code == 200
    response_data = response.json()
    assert response_data["success"] is True

    # Verify task was deleted
    assert not Task.objects.filter(id=task.id).exists()


@pytest.mark.django_db
def test_task_update_view(client):
    user = User.objects.create_user(username="test@example.com", password="securepass")
    client.login(username="test@example.com", password="securepass")

    # Create a task to update
    task = Task.objects.create(user=user, title="Old Title", status=0)

    data = {"title": "Updated Task Title", "status": 1}

    # Send PUT request
    response = client.put(
        reverse("taskmanager:task-update", args=[task.id]),
        json.dumps(data),
        content_type="application/json",
    )

    assert response.status_code == 200
    response_data = response.json()
    assert response_data["success"] is True

    # Verify task was updated in the database
    task.refresh_from_db()
    assert task.title == "Updated Task Title"
    assert task.status == 1


@pytest.mark.django_db
def test_task_list_view(client):
    user = User.objects.create_user(username="test@example.com", password="securepass")
    client.login(username="test@example.com", password="securepass")

    # Create some tasks with different statuses
    Task.objects.create(user=user, title="Todo Task", status=0)
    Task.objects.create(user=user, title="Doing Task", status=1)
    Task.objects.create(user=user, title="Done Task", status=2)

    response = client.get(reverse("taskmanager:task-list"))

    assert response.status_code == 200
    assert "tasks_todo" in response.context
    assert "tasks_doing" in response.context
    assert "tasks_done" in response.context

    # Check the number of tasks in each status
    assert len(response.context["tasks_todo"]) == 1
    assert len(response.context["tasks_doing"]) == 1
    assert len(response.context["tasks_done"]) == 1
