"""This module contain urls for application."""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import ProfileView


name_apps = 'marketplace'


urlpatterns = [
    path('profile', ProfileView.as_view(), name='profile')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
