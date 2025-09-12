from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import ValidationError
from django.utils.html import escape
from .models import Book
from .forms import ExampleForm

# All views are protected by permissions, adding csrf_protect for POST requests
# and get_object_or_404 for safer object retrieval.

@csrf_protect
@permission_required('relationship_app.can_view', raise_exception=True)
@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})


@csrf_protect
@permission_required('relationship_app.can_create', raise_exception=True)
@login_required
def book_create(request):
    if request.method == "POST":
        # Validate and sanitize inputs
        title = escape(request.POST.get('title', '').strip())
        author_id = request.POST.get('author_id')

        if not title:
            raise ValidationError("Title is required.")

        # Use ORM safely (prevents SQL injection)
        Book.objects.create(title=title, author_id=author_id)
        return redirect('book_list')

    return render(request, 'relationship_app/book_form.html')

def example_form_view(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Normally save or process data here
            pass
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
@csrf_protect
@permission_required('relationship_app.can_edit', raise_exception=True)
@login_required
def book_edit(request, book_id):
    # Safer retrieval (returns 404 instead of crashing if not found)
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        new_title = escape(request.POST.get('title', '').strip())
        if not new_title:
            raise ValidationError("Title cannot be empty.")
        book.title = new_title
        book.save()
        return redirect('book_list')

    return render(request, 'relationship_app/book_form.html', {'book': book})


@csrf_protect
@permission_required('relationship_app.can_delete', raise_exception=True)
@login_required
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book_list')
