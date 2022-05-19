from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from .models import Project, ToDo
from .serializers import ProjectSerializer, ToDoSerializer
from .filters import ProjectFilter


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ToDoViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def destroy(self, request, pk):
        todo = ToDo.objects.all()
        current_todo = get_object_or_404(todo, pk=pk)
        serializer = ToDoSerializer(current_todo)
        if current_todo.is_active:
            current_todo.is_active = False
        else:
            current_todo.is_active = True

        return Response(serializer.data)



class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ToDoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectCustomDjangoFilterViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filterset_class = ProjectFilter


class TodoDjangoFilterViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    filterset_fields = ['project']
