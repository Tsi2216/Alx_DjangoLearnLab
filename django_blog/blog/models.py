# blog/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import post_save


# -----------------------------
# PROFILE MODEL
# -----------------------------
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


# Automatically create or update Profile whenever a User is created/updated
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    # When a new user is created, create a Profile
    if created:
        Profile.objects.create(user=instance)
    else:
        # When existing user is saved, ensure profile exists and save it
        instance.profile.save()


# -----------------------------
# POST MODEL
# -----------------------------
class Post(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ['-published_date']  # newest posts first

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Auto-generate slug from title if not provided
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
