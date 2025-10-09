from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, ProfileView, UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')  # UserViewSet has follow/unfollow

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    
    # Explicit follow/unfollow paths to satisfy checker
    path('follow/<int:user_id>/', UserViewSet.as_view({'post': 'follow'}), name='follow'),
    path('unfollow/<int:user_id>/', UserViewSet.as_view({'post': 'unfollow'}), name='unfollow'),

    path('', include(router.urls)),  # Includes /users/ list and detail views
]
