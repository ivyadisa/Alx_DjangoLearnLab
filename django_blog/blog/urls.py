from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # User auth
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    
    # Blog post URLs
    path('post/', views.PostListView.as_view(), name='post-list'),                
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),        
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),   
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),  
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # Comment URLs (nested under post for clarity)
    path('post/<int:pk>/comments/new/', views.add_comment, name='comment-create'),  
    path('comment/<int:pk>/update/', views.update_comment, name='comment-update'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='comment-delete'),
]
