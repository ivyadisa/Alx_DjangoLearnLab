from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from .models import Book

@permission_required('relationship_app.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})

@permission_required('relationship_app.can_create', raise_exception=True)
def book_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author_id = request.POST.get('author_id')
        Book.objects.create(title=title, author_id=author_id)
        return redirect('book_list')
    return render(request, 'relationship_app/book_form.html')

@permission_required('relationship_app.can_edit', raise_exception=True)
def book_edit(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == "POST":
        book.title = request.POST.get('title')
        book.save()
        return redirect('book_list')
    return render(request, 'relationship_app/book_form.html', {'book': book})

@permission_required('relationship_app.can_delete', raise_exception=True)
def book_delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('book_list')
