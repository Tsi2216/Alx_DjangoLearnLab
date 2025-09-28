from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework as filters  # ✅ import django_filters
from rest_framework.filters import OrderingFilter, SearchFilter  # ✅ import DRF filters
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer


# ✅ Custom Book Filter
class BookFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    author = filters.CharFilter(field_name='author__name', lookup_expr='icontains')
    publication_year = filters.NumberFilter()

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']


# ✅ List all books + filtering + searching + ordering
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, searching, ordering
    filterset_class = BookFilter
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering

    # ✅ Explicitly reference backends
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter, SearchFilter]


# ✅ Retrieve a single book
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# ✅ List all authors
class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]


# ✅ Retrieve a single author
class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
