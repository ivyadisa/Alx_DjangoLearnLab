from django.shortcuts import render
from rest_framework import generic
from .models import MyModel
from .serializers import MyModelSerializer


class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
