from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('webpage.urls', namespace='webpage')),
    url(r'^account/', include('account.urls', namespace='account')),
    url(r'^blog/', include('blog.urls', namespace='dynamicblog'))
]
