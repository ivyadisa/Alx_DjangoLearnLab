from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Registration view (checker expects "views.register")
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

    # Books list
    path('', views.list_books, name='home'),
    path('books/', views.list_books, name='list_books'),

    # Library detail
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
