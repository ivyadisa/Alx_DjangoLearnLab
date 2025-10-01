# blog/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post
from django.utils import timezone
from .models import Comment

# -------------------------
# User registration form
# -------------------------
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        help_text='Required. Enter a valid email address.'
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# -------------------------
# User update form
# -------------------------
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

# -------------------------
# Profile update form
# -------------------------
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_image']

# -------------------------
# Post creation / update form
# -------------------------
class PostForm(forms.ModelForm):
    published_date = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'published_date']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter title'}),
            'content': forms.Textarea(attrs={'rows': 8, 'placeholder': 'Write your post...'}),
        }

    def clean_published_date(self):
        data = self.cleaned_data.get('published_date')
        if not data:
            return None
        return data

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a comment...'})
        }
