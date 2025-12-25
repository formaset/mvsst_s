from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("ckeditor5/", include("django_ckeditor_5.urls")),
    path("", include(("core.urls", "core"), namespace="core")),
    path("blog/", include(("blog.urls", "blog"), namespace="blog")),
]

# media в DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# static (добавляем принудительно)
urlpatterns += staticfiles_urlpatterns()
