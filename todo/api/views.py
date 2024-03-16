from django.shortcuts import render, redirect
from task.models import Task
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TaskSerializer


@api_view(['GET'])
def view_task(request):
	task = Task.objects.all()
	serializer = TaskSerializer(task, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def create_task(request):
	serializer = TaskSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['DELETE'])
def delete_task(request, pk):
	task = Task.objects.get(id=pk)
	if task:
		task.delete()
	return Response("deleted")