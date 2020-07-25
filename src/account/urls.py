"""This module contain urls for application."""

from django.urls import path
from .views import test


name_apps = 'account'


urlpatterns = [
    path('', test)
]
