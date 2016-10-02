from django.conf.urls import url
from . import views

urlpatterns = (
    url(r'^$', views.post_list, name='post_list'),
    url(r'^books/(?P<slug>[\w./-]+)/$', views.books, name='books'),
    url(r'^(?P<slug>[\w./-]+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<slug>[\w./-]+)/md$', views.serialize_text, name='serialize_text'),
    url(r'^(?P<slug>[\w./-]+)/update$', views.update, name='update_text'),
    url(r'^search', views.search_posts, name='search_posts'),
)
