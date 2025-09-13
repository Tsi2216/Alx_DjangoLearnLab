# bookshelf/models.py
from django.db import models
from relationship_app.models import CustomUser  # Import your custom user model

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Reference to CustomUser

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Reference to CustomUser
    content = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return f'Review of {self.book.title} by {self.user.username}'