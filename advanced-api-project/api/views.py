from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# List + Create
class BookListCreateView(generics.ListCreateAPIView):
    """
    Handles listing all books and creating new ones.
    GET -> List all books
    POST -> Create a new book (auth required)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Restrict creation to authenticated users only
    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]


# Retrieve a single book
class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve details of a single book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# Update an existing book
class BookUpdateView(generics.UpdateAPIView):
    """
    Update a book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# Delete a book
class BookDeleteView(generics.DestroyAPIView):
    """
    Delete a book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
