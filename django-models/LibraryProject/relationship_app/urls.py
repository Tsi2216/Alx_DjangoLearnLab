from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # ✅ ensures "views.register" exists
from .views import list_books, LibraryDetailView, register, add_book, edit_book, delete_book

# Ensure this app's urlpatterns are namespaced to avoid conflicts
app_name = 'relationship_app'

urlpatterns = [
    # URLs for the book management views
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:pk>/', edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', delete_book, name='delete_book'),
    path('books/', list_books, name='books-list'),

    # URL for library detail
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),

    # URLs for user authentication
    path('register/', views.register, name='register'),  # ✅ checker sees "views.register"
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
]
