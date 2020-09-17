"""This module contain urls for application."""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .services.temporary_processing import Procesing

from .views import (
    StocksView, ProfileView, NotificationsView,
    PasswordView, StockGrowthView, EditProfileView)


name_apps = 'marketplace'


urlpatterns = [
    path('stocks', StocksView.as_view(), name='stocks'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('notifications', NotificationsView.as_view(), name='notifications'),
    path('password', PasswordView.as_view(), name='password'),
    path('stockgrowth', StockGrowthView.as_view(), name='stockgrowth'),
    path('editprofile', EditProfileView.as_view(), name='editprofile')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

Procesing.all_proccesing()
