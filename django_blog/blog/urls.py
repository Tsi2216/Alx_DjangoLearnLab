# blog/urls.py
from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostByTagListView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    search_posts,
    register_view,
    login_view,
    profile_view,
)
from django.contrib.auth.views import LogoutView

app_name = "blog"

urlpatterns = [
    # ---------------------------
    # Post URLs
    # ---------------------------
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    # ---------------------------
    # Comment URLs
    # ---------------------------
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),

    # ---------------------------
    # Tag URLs
    # ---------------------------
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts_by_tag'),

    # ---------------------------
    # Search URL
    # ---------------------------
    path('search/', search_posts, name='search_posts'),

    # ---------------------------
    # Authentication URLs
    # ---------------------------
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    path('logout/', LogoutView.as_view(next_page='blog:login'), name='logout'),
]
