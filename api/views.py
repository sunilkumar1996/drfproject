from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
import json


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = {
        'status': 'request was permitted'
    }
    return Response(content, status=status.HTTP_200_OK)


class UserCreate(APIView):
    """ 
    Creates the user. 
    """

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            print(email)
            # user_exist = User.objects.filter(email=)
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                json['Success'] = True
                return Response(json, status=status.HTTP_201_CREATED)
        context = {
            "success": False,
            "message": "Your Email Already Registred!",
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):

        return Response(status=status.HTTP_200_OK)


class ForgotPassword(APIView):
    """
    Forgot password : User 
    """
    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def post(self, request, format='json'):
        return Response(status=status.HTTP_201_CREATED)