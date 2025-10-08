from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    """Follow a user by ID."""
    try:
        target_user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)

    # Prevent following self
    if target_user == request.user:
        return Response({'error': "You cannot follow yourself"}, status=400)

    # Add target_user to current user's following list
    request.user.following.add(target_user)
    return Response({'success': f'You are now following {target_user.username}'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    """Unfollow a user by ID."""
    try:
        target_user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)

    # Prevent unfollowing self
    if target_user == request.user:
        return Response({'error': "You cannot unfollow yourself"}, status=400)

    # Remove target_user from current user's following list
    request.user.following.remove(target_user)
    return Response({'success': f'You have unfollowed {target_user.username}'})
