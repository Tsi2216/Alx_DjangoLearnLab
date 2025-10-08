from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView

# Create a router for posts and comments
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),             # Include post and comment routes
    path('feed/', FeedView.as_view(), name='feed'),  # Endpoint for user feed
]