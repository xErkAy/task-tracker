from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from account.authentication import admin_login

urlpatterns = [
    # path('admin/login/', admin_login),
    path('admin/', admin.site.urls),
    path('api/', include('account.urls')),
    path('', include('tracker.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
