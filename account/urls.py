"""This module contain urls for application."""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import LoginView, SingupView


name_apps = 'account'


urlpatterns = [
    path('', LoginView.as_view()),
    path('login', LoginView.as_view(), name='login'),
    path('signup', SingupView.as_view(), name='signup')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
