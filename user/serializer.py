from rest_framework import serializers
from .models import Profile


# profile serializer
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("user", "profile_photo", "bio", "contact")