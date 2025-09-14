# your_app/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book, Review
from .forms import BookForm, ReviewForm

@login_required
@permission_required('your_app.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'your_app/book_list.html', {'books': books})

@login_required
@permission_required('your_app.can_create', raise_exception=True)
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'your_app/book_form.html', {'form': form})

@login_required
@permission_required('your_app.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'your_app/book_form.html', {'form': form})

@login_required
@permission_required('your_app.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'your_app/book_confirm_delete.html', {'book': book})

# Example views for Review model
@login_required
@permission_required('your_app.can_create', raise_exception=True)
def review_create(request, book_pk):
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
    return render(request, 'your_app/review_form.html', {'form': form, 'book': book})