# urls.py
from django.urls import path
from .views import add_book, edit_book, delete_book

urlpatterns = [
    path('add/', add_book, name='add_book'),  # URL for adding a book
    path('edit/<int:pk>/', edit_book, name='edit_book'),  # URL for editing a book
    path('delete/<int:pk>/', delete_book, name='delete_book'),  # URL for deleting a book
]
