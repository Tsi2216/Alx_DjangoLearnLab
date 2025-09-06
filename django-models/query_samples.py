from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    """Query all books by a specific author."""
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")

def list_books_in_library(library_name):
    """List all books in a library."""
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library_name}:")
        for book in books:
            print(f"- {book.title} (by {book.author.name})")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")

def retrieve_librarian_for_library(library_name):
    """Retrieve the librarian for a library."""
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        print(f"The librarian for {library_name} is: {librarian.name}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
    except Librarian.DoesNotExist:
        print(f"No librarian found for '{library_name}'.")

def create_sample_data():
    """Helper function to create some data to query."""
    print("Creating sample data...")
    author1, created = Author.objects.get_or_create(name="Jane Austen")
    author2, created = Author.objects.get_or_create(name="George Orwell")

    book1, created = Book.objects.get_or_create(title="Pride and Prejudice", author=author1)
    book2, created = Book.objects.get_or_create(title="1984", author=author2)
    book3, created = Book.objects.get_or_create(title="Sense and Sensibility", author=author1)

    library1, created = Library.objects.get_or_create(name="City Central Library")
    library1.books.set([book1, book2])

    library2, created = Library.objects.get_or_create(name="University Library")
    library2.books.set([book3])

    librarian1, created = Librarian.objects.get_or_create(name="Alice Johnson", library=library1)
    librarian2, created = Librarian.objects.get_or_create(name="Bob Williams", library=library2)
    print("Sample data created successfully.")