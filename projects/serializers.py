from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from projects.models import Project, ToDo
from users.serializers import UserSerializer


class ProjectSerializerBase(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectSerializer(ModelSerializer):
    # user = UserSerializer(many=True)  #  несколько пользователей, работающих над проектом
    # user = UserSerializer()

    class Meta:
        model = Project
        fields = '__all__'


class ToDoSerializer(ModelSerializer):
    # user = UserSerializer()  # пользователь, создающий конкретную заметку по проекту
    # project = ProjectSerializer()

    class Meta:
        model = ToDo
        fields = '__all__'


# project1 = Project.object.create('project1_name', 'https://github.com/team1/project1')
# project1.udsers.add('user1')