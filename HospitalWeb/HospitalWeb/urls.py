from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


admin.site.site_header = "Gainsville hospital"
admin.site.site_title = "Gainsville hospital"
admin.site.index_title = "Welcome Gainsville hospital auth portal"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('management.urls')),
    path('staff/', include('staff.urls')),
    path('bill/', include('bill.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)