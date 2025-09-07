from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import DetailView
from .models import Book, Library

# Function-Based View for listing books
def list_books(request):
    books = Book.objects.all()  # Fetch all Book objects from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View for Library Details
class LibraryDetailView(DetailView):
    model = Library  # Specifies the model to use
    template_name = 'relationship_app/library_detail.html'  # Template to render
    context_object_name = 'library'  # Name of the object in the template context

# Function-Based View for User Registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('list_books')  # Redirect to the books list after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
