# update.md
# Command to update the title of the book
>>> from bookshelf.models import Book
>>> book_to_update = Book.objects.get(title="1984")
>>> book_to_update.title = "Nineteen Eighty-Four"
>>> book_to_update.save()
>>> updated_book = Book.objects.get(pk=book_to_update.pk)
>>> print(updated_book.title)

# Expected Output: The updated title.
Nineteen Eighty-Four
