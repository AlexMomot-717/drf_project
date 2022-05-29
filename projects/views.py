from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.pagination import LimitOffsetPagination
from .models import Project, ToDo
from .serializers import ProjectSerializer, ToDoSerializer
from .filters import ProjectFilter


class ProjectPaginator(LimitOffsetPagination):
    default_limit = 10


class ToDoPaginator(LimitOffsetPagination):
    default_limit = 20


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    # renderer_classes = [JSONRenderer]
    serializer_class = ProjectSerializer
    filterset_class = ProjectFilter
    # pagination_class = ProjectPaginator


class ToDoViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    # renderer_classes = [JSONRenderer]
    serializer_class = ToDoSerializer
    filterset_fields = ['project']
    # pagination_class = ToDoPaginator

    def destroy(self, request, pk):
        todo = self.get_object()
        # serializer = ToDoSerializer(todo)
        if todo.is_active:
            todo.is_active = False
        else:
            todo.is_active = True
        todo.save()

        # return Response(serializer.data)
        return Response(status=status.HTTP_200_OK)
