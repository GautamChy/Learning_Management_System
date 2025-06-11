from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.serializers import ValidationError
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

# Class_based_Views
class LoginAPIView(APIView):
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        if username == None and password == None:
            raise ValidationError({
                'details':'Both username and password required'
            })
        user = authenticate(username=username,password=password)
        if user:
            token,_=Token.objects.get_or_create(user=user)
            return Response({
                'details':'User is registered',
                'token':token.key,
                'username':user.username
            },status=status.HTTP_202_ACCEPTED)
        return Response({
            'details':'User is not registered'
        },status=status.HTTP_401_UNAUTHORIZED)