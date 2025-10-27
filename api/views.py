from django.shortcuts import render
from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSerializer, UserProfileSerializer, UpdateUserProfileSerializer, TodoSerializer, UpdateTodoSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from users.models import CustomUser
from .permissions import IsOwnerOnly
from todos.models import Todo


class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    update_serializer_class = UpdateUserProfileSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ('get', 'put', 'patch', 'head', 'options',)

    def get_queryset(self):
        return CustomUser.objects.filter(pk=self.request.user.pk)
    
    def get_serializer_class(self):
        if self.action in ['update', 'partial_update',]:
            return self.update_serializer_class
        return self.serializer_class
    
class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    update_serializer_class = UpdateTodoSerializer
    permission_classes = [IsAuthenticated, IsOwnerOnly,]
    http_method_names = ('get', 'post', 'put', 'patch','head', 'options', 'delete',)
    
    def get_queryset(self):
        return Todo.objects.filter(author=self.request.user)
    
    def get_serializer_class(self):
        if self.action in ['update', 'partial_update',]:
            return self.update_serializer_class
        return self.serializer_class
    
    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)
    
    
