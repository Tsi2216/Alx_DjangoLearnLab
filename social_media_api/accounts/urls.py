from django.urls import path
from .views import RegisterView, LoginView, ProfileView, UserViewSet
from rest_framework.routers import DefaultRouter

# Create a router for user follow management
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # Endpoint for user registration
    path('login/', LoginView.as_view(), name='login'),            # Endpoint for user login
    path('profile/', ProfileView.as_view(), name='profile'),      # Endpoint for user profile
    path('', include(router.urls)),                                # Include user follow management routes
]