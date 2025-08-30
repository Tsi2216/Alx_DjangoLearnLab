# bookshelf/admin.py
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Customize the list view
    list_display = ('title', 'author', 'publication_year')

    # Add a search bar
    search_fields = ('title', 'author')

    # Add filters on the right sidebar
    list_filter = ('publication_year', 'author')

admin.site.register(Book, BookAdmin)