from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from polls.admin import admin_site  # Yeni admin panelimizi çağırırıq

urlpatterns = [
    path(
        'admin/', admin_site.urls
    ),  # Artıq parol istəməyən admin panel açılacaq
    path('', include('polls.urls')),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)