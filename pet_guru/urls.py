from django.conf import settings
from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls')),
    url(r'^', include('chat.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)