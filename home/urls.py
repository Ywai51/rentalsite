from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index , name="index"),
    path("snkLayanan", views.snkIndex, name="snk"),
    path("search", views.searchView, name="search"),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
