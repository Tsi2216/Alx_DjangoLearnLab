# blog/urls.py
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Authentication
    path('register/', views.register_view, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('profile/', views.profile_view, name='profile'),

    # Posts
    path('', views.PostListView.as_view(), name='post-list'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # Comments
    path('post/<int:post_pk>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),

    # Tags & Search
    path('tags/', views.TagListView.as_view(), name='tag-list'),
    path('tags/<str:tag_name>/', views.TagPostsView.as_view(), name='tag-posts'),
    path('search/', views.SearchView.as_view(), name='search'),

    # Dashboard
    path('dashboard/', views.user_dashboard, name='user-dashboard'),
]
