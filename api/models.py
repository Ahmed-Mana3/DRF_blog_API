from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.text import slugify
from django.utils import timezone
import random
import string


class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', height_field=None, width_field=None, max_length=None, null=True, blank=True) 
    facebook = models.URLField(max_length=200, blank=True, null=True)
    instagram = models.URLField(max_length=200, blank=True, null=True)
    youtube = models.URLField(max_length=200, blank=True, null=True)
    twitter = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.username


class Blog(models.Model):
    CATEGORY = (
        ("Technology", "Technology"),
        ("Economy", "Economy"),
        ("Business", "Business"),
        ("Sports", "Sports"),
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True, blank=True, max_length=255) # New To Know
    content = models.TextField()
    category = models.CharField(max_length=255, choices=CATEGORY, blank=True, null=True)
    blog_image = models.ImageField(upload_to="blog_images/", height_field=None, width_field=None, max_length=None, blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="blogs", null=True) 
    # related_name --> It means: from a User object, you can access their blogs with .blogs
    # null True --> database level (this column can store Null) 
    # blank True --> forms level (Django will require the field to have a value when submitting a form)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    is_draft = models.BooleanField(default=True) 

    class Meta:
        ordering = ["-publish_date"] # new ones first

    def __str__(self):
        return f"{self.title} by {self.author} at ({self.publish_date}) "
    
    def save(self, *args, **kwargs):
        base_slug = slugify(self.title)
        slug = base_slug

        # if slug already exists, add a random character until unique
        while Blog.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{random.choice(string.ascii_letters)}"

        self.slug = slug

        # auto-set publish_time if not draft and not already set
        if not self.is_draft and self.publish_date is None:
            self.publish_time = timezone.now()

        super().save(*args, **kwargs)


