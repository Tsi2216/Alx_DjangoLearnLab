from rest_framework import generics, viewsets       # import viewsets
from .models import Book
from .serializers import BookSerializer

# Existing ListAPIView for reference
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# New ViewSet for full CRUD
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
