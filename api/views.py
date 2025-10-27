from django.shortcuts import render
from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSerializer, UserProfileSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from users.models import CustomUser


class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ('get', 'head', 'options',)

    def get_queryset(self):
        return CustomUser.objects.filter(pk=self.request.user.pk)
