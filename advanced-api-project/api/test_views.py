from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')  # Authenticate

        # Create authors
        self.author1 = Author.objects.create(name='Author One')
        self.author2 = Author.objects.create(name='Author Two')

        # Create books
        self.book1 = Book.objects.create(title='Book One', publication_year=2000, author=self.author1)
        self.book2 = Book.objects.create(title='Book Two', publication_year=2010, author=self.author2)

    # List all books
    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # Retrieve a single book
    def test_retrieve_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    # Create a new book
    def test_create_book(self):
        url = reverse('book-list')
        data = {'title': 'New Book', 'publication_year': 2023, 'author': self.author1.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    # Update a book
    def test_update_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        data = {'title': 'Updated Book', 'publication_year': 2005, 'author': self.author1.id}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book')

    # Delete a book
    def test_delete_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book2.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # Filtering by title
    def test_filter_books_by_title(self):
        url = reverse('book-list') + '?title=Book One'
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book One')

    # Ordering by publication_year
    def test_order_books_by_year(self):
        url = reverse('book-list') + '?ordering=publication_year'
        response = self.client.get(url)
        self.assertEqual(response.data[0]['publication_year'], 2000)

    # Searching by author name
    def test_search_books_by_author(self):
        url = reverse('book-list') + '?search=Author Two'
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], self.author2.id)

    # Permissions test: unauthenticated user
    def test_permissions_unauthenticated(self):
        self.client.logout()
        url = reverse('book-list')
        # GET should work
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # POST should fail
        data = {'title': 'Unauthorized Book', 'publication_year': 2025, 'author': self.author1.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
