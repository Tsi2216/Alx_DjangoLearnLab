from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

# Ensure this app's urlpatterns are namespaced to avoid conflicts
app_name = 'relationship_app'

urlpatterns = [
    # URLs for the book management views
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
    path('books/', views.list_books, name='books-list'),

    # URLs for user authentication
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
]
