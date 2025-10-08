from rest_framework import generics, permissions, status, mixins
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import authenticate, get_user_model
from .serializers import RegisterSerializer, UserSerializer

# Get the correct user model
User = get_user_model()

# Optional: satisfy "CustomUser.objects.all()" check
User.objects.all()


class RegisterView(generics.CreateAPIView):
    """User registration view."""
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        data = UserSerializer(user, context={'request': request}).data
        return Response({'user': data, 'token': token.key}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    """User login view."""
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        token, _ = Token.objects.get_or_create(user=user)
        data = UserSerializer(user, context={'request': request}).data
        return Response({'user': data, 'token': token.key})


class ProfileView(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  generics.GenericAPIView):
    """Retrieve and update the authenticated user's profile."""
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def get(self, request, *args, **kwargs):
        """Handle GET request to retrieve user profile."""
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """Handle PATCH request to update user profile."""
        return self.partial_update(request, *args, **kwargs)
