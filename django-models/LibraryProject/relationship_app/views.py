from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # Ensure Library is imported here

# Function-Based View
def list_books(request):
    books = Book.objects.all()  # Fetch all Book objects from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View
class LibraryDetailView(DetailView):
    model = Library  # Specifies the model to use
    template_name = 'relationship_app/library_detail.html'  # Template to render
    context_object_name = 'library'  # Name of the object in the template context
