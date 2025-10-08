from django.urls import path, include
from .views import (
    RegisterView,
    LoginView,
    ProfileView,
    UserViewSet,
    follow_user,
    unfollow_user
)
from rest_framework.routers import DefaultRouter

# Create a router for user follow management
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),              # User registration
    path('login/', LoginView.as_view(), name='login'),                        # User login
    path('profile/', ProfileView.as_view(), name='profile'),                  # User profile
    path('follow/<int:user_id>/', follow_user, name='follow-user'),           # Follow a user
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow-user'),     # Unfollow a user
    path('', include(router.urls)),                                           # Include UserViewSet routes
]
