from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from main import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('captcha/', include('captcha.urls')),
    path('wewe/', include('wewe.urls')),
]+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)