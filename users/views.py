from rest_framework.generics import (DestroyAPIView, ListAPIView,
                                     RetrieveAPIView, UpdateAPIView, CreateAPIView,)
from rest_framework.viewsets import ModelViewSet

from users.models import Location, User
from users.serializer import *


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    
    
class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
   
   
class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    
    
class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDeleteSerializer
    
    
class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

