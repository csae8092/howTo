import os
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class BlogAuthor(models.Model):
    """ a customized/extended User profile """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    github_name = models.CharField(max_length=250, blank=True)
    redmine_name = models.CharField(max_length=250, blank=True)
    website = models.URLField(blank=True)
    image = models.FileField(upload_to='author_img', blank=True, null=True)

    def __str__(self):
        return self.user.username

    def image_name(self):
        return os.path.basename(self.image.name)


class Book(models.Model):
    """ A 'Book' groups a series of blogs"""
    editor = models.ForeignKey(BlogAuthor, related_name='book_editor')
    title = models.CharField(max_length=250)
    summary = models.TextField(blank=True)
    slug = models.SlugField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to='book_img', blank=True, null=True)
    book_color = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ('title', )

    def __str__(self):
        return self.title

    def image_name(self):
        return os.path.basename(self.image.name)


class Post(models.Model):
    """A Blog-Post objects"""

    STATUS_CHOICES = (
        ('draft', 'draft'),
        ('published', 'published')
    )

    ENCODING_CHOICES = (
        ('TEI', 'TEI'),
        ('markdown', 'markdown')
    )

    AUDIENCE_CHOICES = (
        ('ACDH-CORE', 'ACDH-CORE'),
        ('ACDH-EXTENDED', 'ACDH-EXTENDED'),
        ('PUBLIC', 'PUBLIC'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(BlogAuthor, related_name='blog_posts')
    summary = models.TextField(blank=True)
    body = models.TextField(blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='draft')
    audience = models.CharField(max_length=30, choices=AUDIENCE_CHOICES, default='ACDH-CORE')
    encoding = models.CharField(max_length=30, choices=ENCODING_CHOICES, default='markdown')
    repo_url = models.URLField(blank=True, max_length=300)
    github_url = models.URLField(blank=True, max_length=300)
    tags = TaggableManager()
    book = models.ForeignKey(Book, blank=True, null=True)

    class Meta:
        ordering = ('-publish', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('dynamicblog:post_detail', kwargs={'slug': self.slug})
