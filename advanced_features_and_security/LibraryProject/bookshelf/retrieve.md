# retrieve.md
# Command to retrieve and display the book
>>> from bookshelf.models import Book
>>> retrieved_book = Book.objects.get(title="1984")
>>> print(f"Title: {retrieved_book.title}, Author: {retrieved_book.author}, Year: {retrieved_book.publication_year}")

# Expected Output: The details of the created book.
Title: 1984, Author: George Orwell, Year: 1949
