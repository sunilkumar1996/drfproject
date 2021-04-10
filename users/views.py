from django.shortcuts import render
from rest_framework import generics

from . import serializers
from django.contrib.auth.models import User

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer