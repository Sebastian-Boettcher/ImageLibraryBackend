from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('backend/', include('backend.urls')),
    path('', RedirectView.as_view(url='/backend/', permanent=True)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
