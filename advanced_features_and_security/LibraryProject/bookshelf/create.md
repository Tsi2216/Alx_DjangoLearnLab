# create.md
# Command to create a Book instance
>>> from bookshelf.models import Book
>>> book_1984 = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Expected Output: Successful creation is confirmed by the object representation.
>>> book_1984
<Book: 1984>