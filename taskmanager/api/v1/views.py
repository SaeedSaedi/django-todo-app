from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from ...models import Task
from .serializers import TaskSerializer


class TaskListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get(self, request):
        tasks = Task.objects.filter(user=request.user)
        serializer = self.serializer_class(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_object(self, task_id, user):
        return get_object_or_404(Task, id=task_id, user=user)

    def get(self, request, task_id):
        task = self.get_object(task_id, request.user)
        serializer = self.serializer_class(task)
        return Response(serializer.data)

    def put(self, request, task_id):
        task = self.get_object(task_id, request.user)
        serializer = self.serializer_class(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, task_id):
        task = self.get_object(task_id, request.user)
        task.delete()
        return Response({"detail": "Task deleted."}, status=status.HTTP_204_NO_CONTENT)
