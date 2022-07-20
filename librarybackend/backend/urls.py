from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = "Backend"

urlpatterns = [
    path('', views.index, name='index'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('grid/', views.grid, name='grid'),
    
    path('upload_image/success/',views.success, name='success'),
    path('upload_image/error/',views.error, name='error')
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )