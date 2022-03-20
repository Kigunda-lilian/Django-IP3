from rest_framework import serializers
from .models import  Project

# Project serializer
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
