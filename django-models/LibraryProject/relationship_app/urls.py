# urls.py
from django.urls import path
from .views import add_book, edit_book, delete_book
from .views import list_books", LibraryDetailView

urlpatterns = [
    path('add_book/', add_book, name='add_book'),  # URL for adding a book
    path('edit_book/<int:pk>/', edit_book, name='edit_book'),  # URL for editing a book
    path('delete_book/<int:pk>/', delete_book, name='delete_book'),  # URL for deleting a book
]
