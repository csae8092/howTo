from django import template
from blog.models import Book

register = template.Library()


@register.inclusion_tag('blog/tags/book_list.html')
def book_list():
    books = Book.objects.all()
    return {"books": books}
