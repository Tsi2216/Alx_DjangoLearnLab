from django.db import models

# Create your models here.

class Library(models.Model):
    """
    A model to represent a library building or institution.
    """
    name = models.CharField(max_length=200, help_text="The name of the library.")
    location = models.CharField(max_length=200, help_text="The location of the library.")

    def __str__(self):
        """
        Returns the string representation of the Library object.
        """
        return self.name

class Librarian(models.Model):
    """
    A model to represent a librarian working at a specific library.
    
    This class includes a ForeignKey to link a librarian to a Library instance.
    The on_delete=models.CASCADE ensures that if a Library is deleted,
    all associated Librarian records are also deleted.
    """
    name = models.CharField(max_length=100, help_text="The name of the librarian.")
    library = models.ForeignKey(Library, on_delete=models.CASCADE, help_text="The library where the librarian works.")
    employee_id = models.CharField(max_length=50, unique=True, help_text="The unique employee ID of the librarian.")
    
    def __str__(self):
        """
        Returns the string representation of the Librarian object.
        """
        return f"{self.name} ({self.library.name})"
