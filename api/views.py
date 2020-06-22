
from .serializers import TaskSerializer

from .models import Task
# from django.http import JsonResponse


from rest_framework import viewsets

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
	queryset=Task.objects.all()
	serializer_class=TaskSerializer
	ordering = ['id']
    	
# class TaskListView(ListAPIView):
# 	queryset=Task.objects.all()
# 	serializer_class=TaskSerializer
    	
# class TaskDetailView(RetrieveAPIView):
# 	queryset=Task.objects.all()
# 	serializer_class = TaskSerializer

# class TaskCreateView(CreateAPIView):
# 	queryset=Task.objects.all()
# 	serializer_class = TaskSerializer

# class TaskUpdateView(UpdateAPIView):
# 	queryset=Task.objects.all()
# 	serializer_class = TaskSerializer

# class TaskDeleteView(DestroyAPIView):
# 	queryset=Task.objects.all()
# 	serializer_class = TaskSerializer


# @api_view(['GET'])
# def apiOverview(request):
# 	api_urls = {
# 		'List':'/task-list/',
# 		'Detail View':'/task-detail/<str:pk>/',
# 		'Create':'/task-create/',
# 		'Update':'/task-update/<str:pk>/',
# 		'Delete':'/task-delete/<str:pk>/',
# 		}

# 	return Response(api_urls)

# @api_view(['GET'])
# def taskList(request):
# 	tasks = Task.objects.all().order_by('-id')
# 	serializer = TaskSerializer(tasks, many=True)
# 	return Response(serializer.data)
# @api_view(['GET'])
# def taskDetail(request, pk):
# 	tasks = Task.objects.get(id=pk)
# 	serializer = TaskSerializer(tasks, many=False)
# 	return Response(serializer.data)


# @api_view(['POST'])
# def taskCreate(request):
# 	serializer = TaskSerializer(data=request.data)

# 	if serializer.is_valid():
# 		serializer.save()

# 	return Response(serializer.data)

# @api_view(['POST'])
# def taskUpdate(request, pk):
# 	task = Task.objects.get(id=pk)
# 	serializer = TaskSerializer(instance=task, data=request.data)

# 	if serializer.is_valid():
# 		serializer.save()

# 	return Response(serializer.data)


# @api_view(['DELETE'])
# def taskDelete(request, pk):
# 	task = Task.objects.get(id=pk)
# 	task.delete()

# 	return Response('Item succsesfully delete!')



