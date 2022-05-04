from rest_framework.serializers import HyperlinkedModelSerializer
from projects.models import Project, ToDo
from users.serializers import UserSerializer


class ProjectSerializer(HyperlinkedModelSerializer):
    # user = UserSerializer(many=True)  #  несколько пользователей, работающих над проектом

    class Meta:
        model = Project
        fields = '__all__'


class ToDoSerializer(HyperlinkedModelSerializer):
    # user = UserSerializer()  # пользователь, создающий конкретную заметку по проекту
    # project = ProjectSerializer()

    class Meta:
        model = ToDo
        fields = '__all__'


# project1 = Project.object.create('project1_name', 'https://github.com/team1/project1')
# project1.udsers.add('user1')