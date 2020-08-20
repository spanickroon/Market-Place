"""This module contain urls for application."""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    StocksView, ProfileView, NotificationsView,
    PasswordView, StockGrowthView, ExchangeRatesView, EditProfileView)


name_apps = 'marketplace'


urlpatterns = [
    path('stocks', StocksView.as_view(), name='stocks'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('notifications', NotificationsView.as_view(), name='notifications'),
    path('password', PasswordView.as_view(), name='password'),
    path('stockgrowth', StockGrowthView.as_view(), name='stockgrowth'),
    path('exchangerates', ExchangeRatesView.as_view(), name='exchangerates'),
    path('editprofile', EditProfileView.as_view(), name='editprofile')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
