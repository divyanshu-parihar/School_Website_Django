from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('class12/', views.Class12),
    path('class11/', views.Class11),
    path('player/', views.PLayer),
]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,documents_root=settings.MEDIA_ROOT)