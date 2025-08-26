from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')
        read_only_fields = ('id',)



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = (
            'email', 'password', 'first_name', 'last_name', 'date_of_birth', 'username',
            'phone_number', 'location', 'date_joined', 'token'
        )
        read_only_fields = ('date_joined',)

    def create(self, validated_data):
        user = User.objects.create_user(   
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            date_of_birth=validated_data.get('date_of_birth'),
            phone_number=validated_data.get('phone_number', ''),
            location=validated_data.get('location', '')
        )
        token, created = Token.objects.get_or_create(user=user)
        validated_data['token'] = token.key
        user.token = token.key
        user.save()  # Save the user instance with the new token
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if not email or not password:
            raise serializers.ValidationError("Email and password are required.")

        user = authenticate(email=email, password=password)
        if not user:
            raise serializers.ValidationError("Invalid email or password.")

        attrs['user'] = user
        return attrs
    

