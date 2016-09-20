from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class BlogAuthor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    github_name = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    """A Blog-Post objects"""

    STATUS_CHOICES = (
        ('draft', 'draft'),
        ('published', 'published')
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(BlogAuthor, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish', )

    def __str__(self):
        return self.title
