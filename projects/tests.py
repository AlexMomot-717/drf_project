import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate,APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .views import ProjectViewSet, ToDoViewSet
from .models import Project, ToDo


class TestProjectViewSet(TestCase):
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/projects/')
        view = ProjectViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_detail(self):
        project = Project.objects.create(name='project4', repo_link='https://github.com', user=2)
        client = APIClient()
        response = client.get(f'/api/projects/{project.name}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_edit_admin(self):
    #     project = Project.objects.create(name='project6', repo_link='https://github.com', user=1)
    #     client = APIClient()
    #     admin = User.objects.create_superuser('admin4', 'admin4@admin.com', 'admin11111')
    #     client.login(username='admin4', password='admin11111')
    #     response = client.put(f"/api/projects/{project.id}/", {'name': 'project7', 'repo_link': 'https://github.com', 'user': 1})
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     author = Project.objects.get(id=project.id)
    #     self.assertEqual(project.name, 'project7')
    #     self.assertEqual(project.user, 1)
    #     client.logout()


class TestTodoViewSet(TestCase):
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/todos/')
        view = ToDoViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestProjectViewSet(APITestCase):
    def test_get_list(self):
        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_edit_admin(self):
    #     user = User.objects.create(username='user5', first_name='Bася', last_name='Пупкин', email='vasya@mail.ru')
    #     project = Project.objects.create(name='project1', repo_link='https://github.com', user=3)
    #     admin = User.objects.create_superuser('admin2', 'admin2@admin.com', 'admin71717')
    #     self.client.login(username='admin2', password='admin71717')
    #     response = self.client.put(f'/api/projects/{project.id}/', {'name': 'project7', 'repo_link': 'https://github.com', 'user': 3})
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     project = Project.objects.get(id=project.id)
    #     self.assertEqual(project.name, 'project7')

    # def test_edit_mixer(self):
    #     project = mixer.blend(Project)
    #     admin = User.objects.create_superuser('admin2', 'admin2@admin.com', 'admin71717')
    #     self.client.login(username='admin2', password='admin71717')
    #     response = self.client.put(f'/api/projects/{project.id}/', {'name': 'project7', 'repo_link': 'https://github.com', 'user': project.user})
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     project = Project.objects.get(id=project.id)
    #     self.assertEqual(project.name, 'project7')

    def test_get_detail(self):
        project = mixer.blend(Project, name='my_project')

        response = self.client.get(f'/api/projects/{project.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_project = json.loads(response.content)
        self.assertEqual(response_project['name'], 'my_project')

    # def test_get_detail_user(self):
    #     project = mixer.blend(Project, user__username='user11')
    #     response = self.client.get(f'/api/projects/{project.id}/')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     response_project = json.loads(response.content)
    #     self.assertEqual(response_project['user']['username'], 'user11')

