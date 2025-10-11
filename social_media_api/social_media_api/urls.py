from django.urls import path, include
from django.http import HttpResponse
from django.contrib import admin

def home(request):
    return HttpResponse("Welcome to the Social Media API 🚀")

urlpatterns = [
    path('', include('accounts.urls')),
    path('api/posts/', include('posts.urls')),
]
