from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class BlogAuthor(models.Model):
    """ a customized/extended User profile """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    github_name = models.CharField(max_length=250, blank=True)
    redmine_name = models.CharField(max_length=250, blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.user.username


class Book(models.Model):
    """ A 'Book' groups a series of blogs"""
    editor = models.ForeignKey(BlogAuthor, related_name='book_editor')
    title = models.CharField(max_length=250)
    summary = models.TextField(blank=True)
    slug = models.SlugField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('title', )

    def __str__(self):
        return self.title


class Post(models.Model):
    """A Blog-Post objects"""

    STATUS_CHOICES = (
        ('draft', 'draft'),
        ('published', 'published')
    )

    AUDIENCE_CHOICES = (
        ('ACDH-CORE', 'ACDH-CORE'),
        ('ACDH-EXTENDED', 'ACDH-EXTENDED'),
        ('ALL', 'ALL'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(BlogAuthor, related_name='blog_posts')
    summary = models.TextField(blank=True)
    body = models.TextField(blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    audience = models.CharField(max_length=10, choices=AUDIENCE_CHOICES, default='ACDH-CORE')
    repo_url = models.URLField(blank=True, max_length=300)
    tags = TaggableManager()
    book = models.ForeignKey(Book, blank=True, null=True)

    class Meta:
        ordering = ('-publish', )

    def __str__(self):
        return self.title
