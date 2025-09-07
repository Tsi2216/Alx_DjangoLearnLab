from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # Import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # URL for the books list
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # URL for library detail
    path('register/', views.register, name='register'),  # Add this line for the register view
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # URL for login
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # URL for logout
]
