from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        # fields = ('id', 'username', 'password', 'is_subuser')
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'is_subuser')

        # extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            is_subuser=validated_data.get('is_subuser', False)
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
