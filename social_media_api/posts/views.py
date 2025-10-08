from rest_framework import viewsets, permissions, filters
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only owners to edit/delete their objects.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for anyone
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed for the owner of the object
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    """ViewSet for managing posts."""
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def get_queryset(self):
        """Return posts from users the current user is following, or all posts for anonymous users."""
        user = self.request.user
        if user.is_authenticated:
            # Get users the current user is following
            following_users = user.following.all()  # Make sure your User model has 'following' ManyToMany
            return Post.objects.filter(author__in=following_users).order_by('-created_at')
        # For anonymous users, return all posts
        return Post.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        """Save the post with the current user as the author."""
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet for managing comments."""
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        """Save the comment with the current user as the author."""
        serializer.save(author=self.request.user)
