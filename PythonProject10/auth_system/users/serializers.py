from rest_framework import serializers
from .models import User
import bcrypt

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_repeat = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'middle_name', 'email', 'password', 'password_repeat')

    def validate(self, data):
        if data['password'] != data['password_repeat']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('password_repeat')
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        user = User.objects.create(password_hash=hashed.decode(), **validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()