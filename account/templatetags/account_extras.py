from django import template

register = template.Library()


@register.inclusion_tag('account/tags/login_tag.html')
def login_tag():
    return {"test": "test"}
