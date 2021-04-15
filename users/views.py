from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User

from . import serializers
from django.contrib.auth.models import User

from .serializers import RegisterUserSerializer, ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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