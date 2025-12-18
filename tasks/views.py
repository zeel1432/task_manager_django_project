# from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # 🔐 only logged-in user's tasks
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # auto assign logged-in user
        serializer.save(user=self.request.user)
