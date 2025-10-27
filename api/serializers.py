from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from users.models import CustomUser, Profile


class CustomRegisterSerializer(RegisterSerializer):
    username = None
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    birth_date = serializers.DateField(allow_null=True)

    def custom_signup(self, request, user):
        user.first_name = self.validated_data.get('first_name', '')
        user.last_name = self.validated_data.get('last_name', '')
        user.birth_date = self.validated_data.get('birth_date', '')
        user.save(update_fields=['first_name', 'last_name', 'birth_date',])


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('sex', 'town', 'state', 'country', 'bio',)


class UserProfileSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'birth_date', 'profile',)
        read_only_fields = ('email',)


class UpdateUserProfileSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'birth_date', 'profile',)

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        profile_instance = instance.profile
        super().update(instance, validated_data)
        for attr, value in profile_data.items():
            setattr(profile_instance, attr, value)
        profile_instance.save()
        return instance
    