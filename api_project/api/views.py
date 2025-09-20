from rest_framework import generics                  # required for ListAPIView
from .models import Book                              # your Book model
from .serializers import BookSerializer               # required serializer

class BookList(generics.ListAPIView):                # the DRF ListAPIView
    queryset = Book.objects.all()                    # fetch all books
    serializer_class = BookSerializer                # use BookSerializer
