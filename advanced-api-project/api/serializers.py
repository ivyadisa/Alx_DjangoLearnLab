from rest_framework import serializers
from .models import Author, Book
import datetime


# Book serializer: validates and serializes Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Custom validation: no future publication years
    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# Author serializer: includes nested books
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested relationship

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
