import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from cocktails import urls as cocktail_urls

urlpatterns = [
    path('admin-cocktails-login/', admin.site.urls),
    path('', include(cocktail_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
