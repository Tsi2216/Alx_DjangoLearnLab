from django.urls import path
from .views import BookListView, BookDetailView, AuthorListView, AuthorDetailView

urlpatterns = [
    # ✅ Books
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # ✅ Authors
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
]
