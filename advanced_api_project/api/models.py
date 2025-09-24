from django.db import models

# The Author model stores information about book authors
class Author(models.Model):
    name = models.CharField(max_length=255)  # Author’s name

    def __str__(self):
        return self.name


# The Book model represents books written by authors
class Book(models.Model):
    title = models.CharField(max_length=255)  # Title of the book
    publication_year = models.IntegerField()  # Year of publication
    author = models.ForeignKey(
        Author,
        related_name='books',  # Allows reverse lookup: author.books.all()
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
