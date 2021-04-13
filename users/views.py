from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import serializers
from django.contrib.auth.models import User

from .serializers import RegisterUserSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


# @api_view(['POST', 'GET'])
# def registeruser(request):
#     if request.method == "POST":
#         print("aa gya", request.data)
#         serializer = RegisterUserSerializer(data=request.data)
#         print(serializer)
#         username = serializer.data.get['username']
#         print("Username : ", username)
#         return Response("ok")
#     elif request.method == "GET":
#         content = {
#             "detail": "Authentication credentials were not provided."
#         }
#         return Response(content, status=status.HTTP_200_OK)