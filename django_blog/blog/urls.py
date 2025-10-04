# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Home and Post List
    path('', views.PostListView.as_view(), name='post-list'),

    # Post Details
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),

    # Create, Update, and Delete Posts
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]
