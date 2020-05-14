from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('class12/', views.Class12),
    path('class11/', views.Class11),
    path('player/<classname>/<int:id>', views.PLayer),
]