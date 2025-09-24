from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITestCase(TestCase):
    """✅ Unit tests for Book API endpoints"""

    def setUp(self):
        # Test client
        self.client = APIClient()

        # Create user for authentication
        self.user = User.objects.create_user(username="testuser", password="password123")

        # Create an author
        self.author = Author.objects.create(name="Test Author")

        # Create a book
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2020,
            author=self.author
        )

        # Endpoints
        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", args=[self.book.id])
        self.create_url = reverse("book-create")
        self.update_url = reverse("book-update", args=[self.book.id])
        self.delete_url = reverse("book-delete", args=[self.book.id])

    def test_list_books(self):
        """✅ Test GET all books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_book(self):
        """✅ Test GET single book"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Book")

    def test_create_book_requires_authentication(self):
        """❌ Unauthenticated user should be denied"""
        data = {"title": "New Book", "publication_year": 2023, "author": self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        """✅ Authenticated user can create"""
        self.client.login(username="testuser", password="password123")
        data = {"title": "New Book", "publication_year": 2023, "author": self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book_authenticated(self):
        """✅ Authenticated user can update"""
        self.client.login(username="testuser", password="password123")
        data = {"title": "Updated Book", "publication_year": 2021, "author": self.author.id}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_delete_book_authenticated(self):
        """✅ Authenticated user can delete"""
        self.client.login(username="testuser", password="password123")
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books_by_title(self):
        """✅ Test filtering by title"""
        response = self.client.get(self.list_url, {"title": "Test Book"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books_by_title(self):
        """✅ Test searching books"""
        response = self.client.get(self.list_url, {"search": "Test"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Test" in book["title"] for book in response.data))

    def test_order_books_by_year(self):
        """✅ Test ordering books"""
        Book.objects.create(title="Another Book", publication_year=2018, author=self.author)
        response = self.client.get(self.list_url, {"ordering": "publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years))
