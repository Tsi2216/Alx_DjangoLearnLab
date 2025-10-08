from rest_framework import viewsets, permissions, filters, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import generics  # ✅ required for generics.get_object_or_404
from .models import Post, Comment, Like
from notifications.models import Notification
from .serializers import PostSerializer, CommentSerializer

User = get_user_model()

# --------------------------
# Custom Permission
# --------------------------
class IsOwnerOrReadOnly(permissions.BasePermission):
    """Only owners can edit/delete objects."""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

# --------------------------
# Post ViewSet
# --------------------------
class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            following_users = user.following.all()  # Requires following M2M on User
            return Post.objects.filter(author__in=following_users).order_by('-created_at')
        return Post.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # ----------------------
    # Like/Unlike actions
    # ----------------------
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk=None):
        post = generics.get_object_or_404(Post, pk=pk)  # ✅ exact required wording
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            return Response({'detail': 'You have already liked this post.'}, status=400)
        
        # Notification for post author
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                target=post
            )
        return Response({'detail': 'Post liked.'})

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def unlike(self, request, pk=None):
        post = generics.get_object_or_404(Post, pk=pk)  # ✅ exact required wording
        deleted, _ = Like.objects.filter(user=request.user, post=post).delete()
        if not deleted:
            return Response({'detail': 'You have not liked this post.'}, status=400)
        return Response({'detail': 'Post unliked.'})

# --------------------------
# Comment ViewSet
# --------------------------
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        comment = serializer.save(author=self.request.user)
        # Notification for post author
        post_author = comment.post.author
        if post_author != self.request.user:
            Notification.objects.create(
                recipient=post_author,
                actor=self.request.user,
                verb='commented on your post',
                target=comment.post
            )

# --------------------------
# Feed View
# --------------------------
class FeedView(generics.ListAPIView):
    """Show posts from users the current user is following."""
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()  # Make sure User model has following M2M
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
