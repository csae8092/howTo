from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('webpage.urls', namespace='webpage')),
    url(r'^account/', include('account.urls', namespace='account')),
    url(r'^blog/', include('blog.urls', namespace='dynamicblog'))
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
