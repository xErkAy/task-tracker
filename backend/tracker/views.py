from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import User
from tracker.models import Task, Tag
from tracker.serializers import TaskSerializer, UserSerializer, TagSerializer


class TaskListAPIView(ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.select_related('performer', 'author').prefetch_related('tags')


class TaskDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    lookup_field = 'id'
    queryset = Task.objects.select_related('performer', 'author').prefetch_related('tags')


class TaskInfoAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            'users': UserSerializer(User.objects.all(), many=True).data,
            'tags': TagSerializer(Tag.objects.all(), many=True).data
        })
