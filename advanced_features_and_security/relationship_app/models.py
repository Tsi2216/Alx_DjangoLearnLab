from django.db import models

class Author(models.Model):
    """
    The Author model represents a person who writes books.
    It has a single CharField for the author's name.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    The Book model represents a single publication.
    It has a title and a ForeignKey relationship to an Author.
    This establishes a one-to-many relationship: one author can have many books.
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Library(models.Model):
    """
    The Library model represents a collection of books.
    It has a ManyToManyField relationship to the Book model,
    meaning a library can have many books, and a book can be in many libraries.
    """
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    """
    The Librarian model represents an employee.
    It has a OneToOneField relationship to the Library model,
    meaning a librarian is uniquely assigned to one library, and each library
    has a single librarian.
    """
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    