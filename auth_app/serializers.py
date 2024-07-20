from rest_framework import serializers
from .models import User, Otp
from django.db import models


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['email']

class OtpSerializer(serializers.Serializer):
    email = serializers.EmailField()


class OtpVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6) 