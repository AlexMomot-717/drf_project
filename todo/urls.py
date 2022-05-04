from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from projects.views import ProjectViewSet, ToDoViewSet


router = DefaultRouter()
router.register('users', UserViewSet)
router.register('projects', ProjectViewSet)
router.register('todo', ToDoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
]
