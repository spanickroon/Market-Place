"""This module contain urls for application."""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import LoginView, SingupView


name_apps = 'account'


urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('singup', SingupView.as_view(), name='singup')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
