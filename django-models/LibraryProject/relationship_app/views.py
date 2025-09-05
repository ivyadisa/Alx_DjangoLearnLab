from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Book, Library


# --------------------------
# Function-based View
# --------------------------
def list_books(request):
    books = Book.objects.all()
    output = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return HttpResponse(output, content_type="text/plain")


# --------------------------
# Class-based View
# --------------------------
class LibraryDetailView(DetailView):
    model = Library

    def render_to_response(self, context, **response_kwargs):
        library = context["library"]
        books = library.books.all()
        output = f"Library: {library.name}\n"
        output += "\n".join([f"{book.title} by {book.author.name}" for book in books])
        return HttpResponse(output, content_type="text/plain")
