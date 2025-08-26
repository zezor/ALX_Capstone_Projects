from logging import raiseExceptions
from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(email=request.data['email'])
        token, created = Token.objects.get_or_create(user=user)
        response.data['message'] = 'User registered successfully'
        response.data['token'] = token.key
        return response

    

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]  # Allow any user to access this view

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        # return Response({'user': UserSerializer(user).data})
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': UserSerializer(user).data},status=200)



class LogoutView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(status=204)

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.AllowAny]
    pagination_class = [permissions.IsAdminUser]

    def get_object(self):
        return self.request.user
    

class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = [permissions.IsAdminUser]  # Only allow admin users to access this view

    def get_object(self):
        return self.request.user
    
