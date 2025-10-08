from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth import authenticate, get_user_model
from .serializers import RegisterSerializer, UserSerializer

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    """View for user registration."""
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        # Use serializer to create user and token
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)  # Create token if it doesn't exist
        data = UserSerializer(user, context={'request': request}).data
        return Response({'user': data, 'token': token.key}, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    """View for user login."""
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        token, _ = Token.objects.get_or_create(user=user)  # Create token if it doesn't exist
        data = UserSerializer(user, context={'request': request}).data
        return Response({'user': data, 'token': token.key})

class ProfileView(generics.RetrieveUpdateAPIView):
    """View for retrieving and updating user profile."""
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """Get the current authenticated user."""
        return self.request.user

    def patch(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)  # Return updated user data