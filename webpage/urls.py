from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.start_view, name="start"),
    url(r'^imprint/$', views.imprint_view, name='imprint'),
    url(r'^project-info/$', views.project_info, name='project_info'),
]
