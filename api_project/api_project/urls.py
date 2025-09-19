
from django.contrib import admin
from django.urls import path
from .views import BookListCreateAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/book', views.BookListCreateAPIView.as_view(), name="book_list_create")
]
