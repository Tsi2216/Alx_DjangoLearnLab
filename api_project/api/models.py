from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)   # field: title
    author = models.CharField(max_length=100)  # field: author

    def __str__(self):
        return f"{self.title} by {self.author}"

