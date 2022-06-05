from django.contrib import admin
from django.urls import path, include, re_path
from graphene_django.views import GraphQLView
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from users.views import UserCustomViewSet
from projects.views import ProjectViewSet, ToDoViewSet
# from users.views import UserViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="ToDo",
        default_version='0.1',
        description="Documentation to out project",
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
# router.register('users', UserViewSet)
router.register('users', UserCustomViewSet)
router.register('projects', ProjectViewSet)
router.register('todos', ToDoViewSet)
# router.register('todo', ToDoViewSet, basename='todo')
# router.register('project', ProjectViewSet, basename='project')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    # path('viewsets/', include(router.urls)),
    path('api/', include(router.urls)),
    path('destroy/<int:pk>/', ToDoViewSet.destroy),
    path('api-token-auth/', views.obtain_auth_token),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("graphql/", GraphQLView.as_view(graphiql=True)),

]