# from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        queryset = Task.objects.filter(user=self.request.user)

        # 🔐 only logged-in user's tasks
        completed = self.request.query_params.get("completed")
        priority = self.request.query_params.get("high")
        # print(self.request.query_params)

        # filter by completed
        if completed is not None:
            queryset = queryset.filter(
                completed=completed.lower() == 'true'
            )

        # filter by priority
        if priority is not None:
            queryset = queryset.filter(priority=priority)

            
        return queryset

    def perform_create(self, serializer):
        # auto assign logged-in user
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def completed(self, request, pk=None):
        task = self.get_object()   # fetch task by ID (and user)

        task.completed = True
        task.save()

        return Response(
            {"message": "Task marked as completed"},
            status=status.HTTP_200_OK
    )