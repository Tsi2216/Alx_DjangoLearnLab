# bookshelf/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book, Review
from .forms import BookForm, ReviewForm

@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """
    View to list all books. The query `Book.objects.all()` uses Django's
    ORM, which protects against SQL injection.
    """
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    """
    View to create a new book. Uses Django Forms for input validation and
    the ORM for safe database saving. The {% csrf_token %} tag in the template
    protects against CSRF attacks.
    """
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form})

@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    """
    View to edit an existing book. Uses `get_object_or_404` to securely
    retrieve the book by its primary key (pk) and Django Forms to handle
    the updated data safely.
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/book_form.html', {'form': form})

@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    """
    View to delete a book. Uses `get_object_or_404` for secure object
    retrieval. The ORM's `delete()` method is a safe operation.
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})

# Example views for Review model
@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def review_create(request, book_pk):
    """
    View to create a review. User input for the review is validated and
    sanitized by Django Forms, protecting against XSS and other attacks.
    """
    book = get_object_or_404(Book, pk=book_pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            return redirect('book_detail', pk=book_pk)
    else:
        form = ReviewForm()
    return render(request, 'bookshelf/review_form.html', {'form': form, 'book': book})