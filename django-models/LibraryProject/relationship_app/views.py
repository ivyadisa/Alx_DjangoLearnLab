from django.shortcuts import render
from django.views.generic.detail import DetailView 
from .models import Book
from .models import Library
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

# Function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})
#class function
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

# Register view
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after registration
            messages.success(request, "Registration successful.")
            return redirect("home")  # redirect to homepage or dashboard
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "You are now logged in.")
            return redirect("home")  # redirect after login
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})


# Logout view
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return render(request, "relationship_app/logout.html")