from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', )


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ('email', 'username', "password")