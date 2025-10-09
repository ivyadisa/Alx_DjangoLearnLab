from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

def profile_image_upload_path(instance, filename):
    return f'users/{instance.username}/profile/{filename}'

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to=profile_image_upload_path, blank=True, null=True)
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
        blank=True
    )
    def __str__(self):
        return self.username
