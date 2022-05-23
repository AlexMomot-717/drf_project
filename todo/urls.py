from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from users.views import UserCustomViewSet
from projects.views import ProjectViewSet, ToDoViewSet
# from users.views import UserViewSet

router = DefaultRouter()
# router.register('users', UserViewSet)
router.register('users', UserCustomViewSet)
router.register('projects', ProjectViewSet)
router.register('todo', ToDoViewSet)
# router.register('todo', ToDoViewSet, basename='todo')
# router.register('project', ProjectViewSet, basename='project')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('viewsets/', include(router.urls)),
    path('destroy/<int:pk>/', ToDoViewSet.destroy),
    path('api-token-auth/', views.obtain_auth_token)
]