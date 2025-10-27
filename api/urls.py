from django.urls import path, include
from .views import CustomRegisterView


urlpatterns = [
    path('registration/', CustomRegisterView.as_view(), name='register'),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('', include('dj_rest_auth.urls')),
]
