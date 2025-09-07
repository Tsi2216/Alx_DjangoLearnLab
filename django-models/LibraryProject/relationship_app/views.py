from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

def list_books(request):
    """Function-based view to list all books."""
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    """Class-based view to display a specific library's details."""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'