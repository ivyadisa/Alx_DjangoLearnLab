from django.urls import path, include
from .views import BookList  
from rest_framework.routers import DefaultRouter
from .views import  BookViewSet

#Router set up
router=DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns=[
    path('books/', BookList.as_view(), name='book=list'),

    #view set crud
    path('', include(router.urls))
]