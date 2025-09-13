from django.core.management.base import BaseCommand
from bookshelf.models import Book

class Command(BaseCommand):
    help = 'Create a book entry'

    def handle(self, *args, **kwargs):
        book = Book(title="1984", author="George Orwell", publication_year=1949)
        book.save()
        self.stdout.write(self.style.SUCCESS('Book created: 1984 by George Orwell'))