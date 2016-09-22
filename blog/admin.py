from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import BlogAuthor, Post, Book


class BlogAuthorInline(admin.StackedInline):
    model = BlogAuthor
    can_delete = False
    verbose_name_plural = 'BlogAuthor'


class UserAdmin(BaseUserAdmin):
    inlines = (BlogAuthorInline, )


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Post)
admin.site.register(Book)
