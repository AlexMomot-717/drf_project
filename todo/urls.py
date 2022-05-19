from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users import views
from projects.views import ProjectViewSet, ToDoViewSet
# from users.views import UserViewSet

router = DefaultRouter()
# router.register('users', UserViewSet)
router.register('projects', ProjectViewSet)
router.register('todo', ToDoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
    path('generic/retrieve/<int:pk>/', views.UserRetrieveAPIView.as_view()),
    path('generic/update/<int:pk>/', views.UserUpdateAPIView.as_view()),
]
