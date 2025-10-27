from django.urls import path, include
from .views import CustomRegisterView, UserProfileViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'profiles', UserProfileViewSet, basename='profile')


urlpatterns = [
    path('registration/', CustomRegisterView.as_view(), name='register'),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('', include('dj_rest_auth.urls')),
    path('', include(router.urls)),
]
