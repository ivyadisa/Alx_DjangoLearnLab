from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register_view, list_books, LibraryDetailView

urlpatterns = [
    # Registration view (custom)
    path('register/', register_view, name='register'),

    # Login view (built-in)
    path(
        'login/',
        LoginView.as_view(template_name='relationship_app/login.html'),
        name='login'
    ),

    # Logout view (built-in)
    path(
        'logout/',
        LogoutView.as_view(template_name='relationship_app/logout.html'),
        name='logout'
    ),

    # Books list (function-based view)
    path('', list_books, name='home'),  
    path('books/', list_books, name='list_books'),

    # Library detail (class-based view)
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
