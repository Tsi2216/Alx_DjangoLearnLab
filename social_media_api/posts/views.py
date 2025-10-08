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
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']  # Search by title or content

    def perform_create(self, serializer):
        """Save the post with the current user as the author."""
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet for managing comments."""
    queryset = Comment.objects.all().order_by('-created_at')
    serializer