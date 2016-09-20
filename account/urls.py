from django.conf.urls import url
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^login/$', login, name='login', kwargs={'template_name': 'account/login.html'}),
    url(r'^logout/$', logout, name='logout', kwargs={'template_name': 'account/logout.html'}),
]
