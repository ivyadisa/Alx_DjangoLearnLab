from django.urls import path
from .views import register_view, login_view, logout_view, list_books, LibraryDetailView


urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', list_books, name='home'),  # optional home
    path('books/', list_books, name='list_books'),   # function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # class-based view
]
