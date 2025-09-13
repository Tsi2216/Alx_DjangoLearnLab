from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Library, Book
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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
    

def register(request):
    """
    Function-based view to handle user registration.

    This view uses Django's UserCreationForm to create a new user.
    If the form is valid, it saves the user, logs them in, and redirects.
    Otherwise, it displays the form for the user to fill out.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('relationship_app:books-list')  # Redirect to the books list page
    else:
        form = UserCreationForm()
    
    context = {'form': form}
    return render(request, 'relationship_app/register.html', context)