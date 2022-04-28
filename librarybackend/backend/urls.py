from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = "Backend"

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('grid/', views.grid, name='grid'),
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )