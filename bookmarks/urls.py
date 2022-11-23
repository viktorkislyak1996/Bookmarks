from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from bookmarks import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls'))
]
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
