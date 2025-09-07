from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # Make sure this import is included

class LibraryDetailView(DetailView):
    """Class-based view to display a specific library's details and list all books."""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        """Add books related to the library to the context."""
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(library=self.object)  # Assuming Book has a ForeignKey to Library
        return context