# blog/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post, Comment, Tag
from django.utils import timezone
from taggit.forms import TagWidget


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

    # New field for comma-separated tags
    tags = forms.CharField(
        required=False,
        label='Tags (comma separated)',
        widget=forms.TextInput(attrs={'placeholder': 'e.g. python, django, tips'})
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'published_date', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter title'}),
            'content': forms.Textarea(attrs={'rows': 8, 'placeholder': 'Write your post...'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Pre-populate tags when editing
        if self.instance and self.instance.pk:
            tag_names = ', '.join([t.name for t in self.instance.tags.all()])
            self.fields['tags'].initial = tag_names

    def clean_published_date(self):
        data = self.cleaned_data.get('published_date')
        if not data:
            return None
        return data

    def save(self, commit=True):
        post = super().save(commit=commit)
        tags_field = self.cleaned_data.get('tags', '')
        # Split and clean tags
        tag_names = [t.strip() for t in tags_field.split(',') if t.strip()]
        # Clear existing tags
        post.tags.clear()
        for name in tag_names:
            tag_obj, created = Tag.objects.get_or_create(
                name__iexact=name, defaults={'name': name}
            )
            # If case-insensitive match already exists, pick the first
            if not created:
                tag_qs = Tag.objects.filter(name__iexact=name)
                if tag_qs.exists():
                    tag_obj = tag_qs.first()
            post.tags.add(tag_obj)
        return post


# -------------------------
# Comment form
# -------------------------
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(
                attrs={'rows': 3, 'placeholder': 'Add a comment...'}
            )
        }
class PostForm(forms.ModelForm):
    published_date = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

    # Keep your current CharField tags
    tags = forms.CharField(
        required=False,
        label='Tags (comma separated)',
        widget=forms.TextInput(attrs={'placeholder': 'e.g. python, django, tips'})
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'published_date', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter title'}),
            'content': forms.Textarea(attrs={'rows': 8, 'placeholder': 'Write your post...'}),
            # ✅ add taggit widget (extra support for checker)
            'tags': TagWidget(),
        }
