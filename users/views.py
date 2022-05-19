from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
# from rest_framework import viewsets
# from rest_framework.generics import get_object_or_404
from rest_framework.renderers import JSONRenderer
# from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserSerializer


# class UserViewSet(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class UserListAPIView(ListAPIView):
    renderer_classes = [JSONRenderer]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveAPIView(RetrieveAPIView):
    renderer_classes = [JSONRenderer]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateAPIView(UpdateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = User.objects.all()
    serializer_class = UserSerializer

