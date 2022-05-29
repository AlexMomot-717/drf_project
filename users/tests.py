from django.contrib.auth.base_user import BaseUserManager
from django.test import TestCase
import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate,APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .views import UserCustomViewSet
from .models import User


class TestUserViewSet(TestCase):
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        view = UserCustomViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_create_guest(self):
    #     factory = APIRequestFactory()
    #     request = factory.post('/api/users/', {'username': 'user5', 'first_name': 'Bася', 'last_name': 'Пупкин', 'email': 'vasya@mail.ru'}, format='json')
    #     view = UserCustomViewSet.as_view({'post': 'create'})
    #     response = view(request)
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # def test_create_admin(self):
    #     factory = APIRequestFactory()
    #     request = factory.post('/api/users/', {'username': 'user5', 'first_name': 'Bася', 'last_name': 'Пупкин', 'email': 'vasya@mail.ru'}, format='json')
    #     admin = User.objects.create_superuser('admin2', 'admin2@admin.com', 'admin71717')
    #     force_authenticate(request, admin)
    #     view = UserCustomViewSet.as_view({'post': 'create'})
    #     response = view(request)
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
