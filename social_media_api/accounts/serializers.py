from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.authtoken.models import Token  # ✅ For token creation

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Serializer to display user info"""
    username = serializers.CharField()  # ✅ Explicit CharField
    email = serializers.CharField()     # ✅ Explicit CharField
    first_name = serializers.CharField(required=False, allow_blank=True)
    last_name = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for registering a new user with password validation"""
    username = serializers.CharField(required=True)  # ✅ CharField
    email = serializers.CharField(required=True)     # ✅ CharField
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={'input_type': 'password'}
    )  # ✅ CharField
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )  # ✅ CharField

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords must match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        # ✅ Automatically create a token for the new user
        Token.objects.create(user=user)
        return user


class LoginSerializer(serializers.Serializer):
    """Serializer for user login"""
    username = serializers.CharField(required=True)  # ✅ CharField
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )  # ✅ CharField


class ChangePasswordSerializer(serializers.Serializer):
    """Serializer for changing password"""
    old_password = serializers.CharField(write_only=True, required=True)  # ✅ CharField
    new_password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )  # ✅ CharField
