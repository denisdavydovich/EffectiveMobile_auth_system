from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import RegisterSerializer, LoginSerializer
import bcrypt
import jwt
from django.conf import settings

SECRET_KEY = "SECRET_KEY_FOR_JWT"  # заменить на settings.SECRET_KEY

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            try:
                user = User.objects.get(email=email, is_active=True)
            except User.DoesNotExist:
                return Response({"error": "Invalid credentials"}, status=401)
            if bcrypt.checkpw(password.encode(), user.password_hash.encode()):
                token = jwt.encode({"user_id": str(user.id)}, SECRET_KEY, algorithm="HS256")
                return Response({"token": token})
            return Response({"error": "Invalid credentials"}, status=401)
        return Response(serializer.errors, status=400)

class LogoutView(APIView):
    def post(self, request):
        # Для JWT можно просто удалять на клиенте
        return Response({"message": "Logged out"}, status=200)