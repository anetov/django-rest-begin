from django.shortcuts import render
from .models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import TaskListSerializer

# Create your views here.
@api_view(['GET'])
def list_tasks(request):
    queryset = Task.objects.all()
    serializer = TaskListSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)