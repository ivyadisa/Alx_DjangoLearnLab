from django.db import models

# Author model stores information about book authors
class Author(models.Model):
    name = models.CharField(max_length=255)  # Name of the author

    def __str__(self):
        return self.name


# Book model stores information about individual books
class Book(models.Model):
    title = models.CharField(max_length=255)  # Title of the book
    publication_year = models.IntegerField()  # Year the book was published
    author = models.ForeignKey(
        Author,
        related_name="books",  # Allows accessing an author's books as author.books.all()
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
