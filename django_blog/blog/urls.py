from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # authentication
    path('register/', views.register_view, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('profile/', views.profile_view, name='profile'),

    # posts CRUD
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('posts/new/', views.PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]
