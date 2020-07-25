"""This module contain urls for application."""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import test


name_apps = 'account'


urlpatterns = [
    path('', test)
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
