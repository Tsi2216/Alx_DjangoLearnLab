from django.db import models

# Author model -> represents book authors
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Book model -> each book is linked to an Author (One-to-Many)
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
