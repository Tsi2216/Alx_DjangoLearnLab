from django.db import models

# Create your models here.

class Author(models.Model):
    """
    A model to represent a book's author.
    
    This class defines the fields for an Author, such as their name.
    The `__str__` method is overridden to provide a human-readable representation
    of the object, which is useful in the Django admin interface.
    """
    name = models.CharField(max_length=100, help_text="The name of the author.")

    def __str__(self):
        """
        Returns the string representation of the Author object.
        """
        return self.name

class Book(models.Model):
    """
    A model to represent a book.
    
    This class includes a ForeignKey field to link a book to its author.
    """
    title = models.CharField(max_length=200, help_text="The title of the book.")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, help_text="The author of the book.")
    publication_date = models.DateField(null=True, blank=True)

    def __str__(self):
        """
        Returns the string representation of the Book object.
        """
        return self.title
