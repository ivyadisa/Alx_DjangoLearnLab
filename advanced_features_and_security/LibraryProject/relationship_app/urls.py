from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import list_books   
from .views import LibraryDetailView  
from .views import (
    admin_view,
    librarian_view,
    member_view,
    add_book,
    edit_book,
    delete_book
)

urlpatterns = [
    # Registration view
    path('register/', views.register_view, name='register'),

    # Login view
    path(
        'login/',
        LoginView.as_view(template_name='relationship_app/login.html'),
        name='login'
    ),

    # Logout view
    path(
        'logout/',
        LogoutView.as_view(template_name='relationship_app/logout.html'),
        name='logout'
    ),

    # Books list / home
    
    path('', views.list_books, name='home'),
    path('books/', views.list_books, name='list_books'),

    # Library detail
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    #path('library_detail/<int:id>/', views.library_detail, name='detail'),

    # Role-based views
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),

    # Book CRUD views
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:pk>/', edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', delete_book, name='delete_book'),
]
