# delete.md
# Command to delete the book instance and confirm deletion
<<<<<<< HEAD
```python
>>> from bookshelf.models import Book
>>> book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
>>> book_to_delete.delete()
>>> all_books = Book.objects.all()
>>> print(all_books)
=======
>>> from bookshelf.models import Book
>>> book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
>>> book_to_delete.delete()
(1, {'bookshelf.Book': 1})
>>> all_books = Book.objects.all()
>>> print(all_books)

# Expected Output: An empty QuerySet, confirming the deletion.
<QuerySet []>
>>>>>>> c995c4d2450951ad2ca07e778224a67cdde69e35
