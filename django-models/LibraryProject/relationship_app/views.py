from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library

def list_books(request):
    """
    Function-based view to display a list of all books.
    
    This view fetches all Book objects from the database and passes them
    to the 'list_books.html' template for rendering.
    """
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    """
    Class-based view to display details of a specific library.
    
    This view automatically fetches a Library object based on the primary key
    (pk) in the URL and passes it to the 'library_detail.html' template.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
