from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # User auth
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    
    # Blog post URLs (singular 'post/')
    path('post/', views.PostListView.as_view(), name='post-list'),                # List all posts
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),        # Create new post
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),   # Post detail
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),  # Update post
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),  # Delete post
]
