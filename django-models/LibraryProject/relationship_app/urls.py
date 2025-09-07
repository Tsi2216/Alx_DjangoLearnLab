from django.urls import path
from django.contrib.auth import views as auth_views  # Import auth views
from .views import list_books, LibraryDetailView, register  # Import your views

urlpatterns = [
    path('books/', list_books, name='list_books'),  # URL for the function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL for the class-based view
    path('register/', register, name='register'),  # URL for user registration
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # URL for login
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # URL for logout
]
